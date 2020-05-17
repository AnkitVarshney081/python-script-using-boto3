# 

import boto3
import pprint
session=boto3.Session(profile_name='default')
vpc=session.resource(service_name='ec2', region_name='ap-south-1')

# Create VPC

vpc_cidr = raw_input("Enter VPC Cidr: ")                       # Example - Cidr = 10.200.0.0/16
subnet_cidr = raw_input("Enter Public Subnet Cidr: ") 	       # Example - Cidr = 10.200.0.0/24

vpc_id = vpc.create_vpc(
    CidrBlock=vpc_cidr,					      # IPv4 CIDR block with the VPC
    AmazonProvidedIpv6CidrBlock=False,                        # I do not associate an IPv6 CIDR block with the VPC
    InstanceTenancy='default'			              # You can run instances in your VPC on single-tenant, dedicated hardware. 
							      #	Select Dedicated to ensure that instances launched in this VPC are dedicated tenancy instances, 
	                                                      # regardless of the tenancy attribute specified at launch. 
	                                                      # Select Default to ensure that instances launched in this VPC use the tenancy attribute specified at launch
)

print vpc_id.id   # Example vpc.id = vpc-031b9119cd3ea4078

# Create Public Subnet

response = vpc.create_subnet(
    AvailabilityZone='ap-south-1a',                           # you can choose any Availablity Zone in selected Region
    CidrBlock=subnet_cidr,				      # IPv4 CIDR block with the Subnet = 10.200.0.0/24
    VpcId=vpc_id.id                                           # Associate subnet with vpc
)
print response.id						# Subnet Id

# Create Route Table

route_table = vpc.create_route_table(
    VpcId=vpc_id.id                                           # Associate Route Table with VPC
)

print route_table.id						# Id of Route Table

# Create Internet Gateway

internet_gateway = vpc.create_internet_gateway()

print internet_gateway.id

vpc_cli=session.client(service_name='ec2', region_name='ap-south-1')

# Attach Internet Gateway with VPC

vpc_cli.attach_internet_gateway(
    InternetGatewayId=internet_gateway.id,
    VpcId=vpc_id.id
)

# Subnet Associations - Route Table

ass_rt = vpc_cli.associate_route_table(
    RouteTableId= route_table.id,
    SubnetId= response.id
)

print "Associate rt with subnet"

route = vpc_cli.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId= internet_gateway.id,
    RouteTableId= route_table.id
)

print "Add route"

pubSecGrp = vpc.create_security_group(DryRun=False,
                                      GroupName='pubSecGrp',
                                      Description='Public_Security_Group',
                                      VpcId=vpc_id.id
                                      )

vpc_cli.authorize_security_group_ingress(GroupId=pubSecGrp.id,
                                           IpProtocol='tcp',
                                           FromPort=22,
                                           ToPort=22,
                                           CidrIp='0.0.0.0/0'
                                           )

vpc_cli.authorize_security_group_ingress(GroupId=pubSecGrp.id,
                                           IpProtocol='tcp',
                                           FromPort=80,
                                           ToPort=80,
                                           CidrIp='0.0.0.0/0'
                                           )

userDataCode = """
#!/bin/bash
yum install -y httpd
echo "Welcome To My Website" > /var/www/html/index.html
service httpd start
chkconfig httpd on
"""

instance = vpc.create_instances(ImageId='ami-0470e33cd681b2476',
                                   MinCount=1,
                                   MaxCount=1,
                                   KeyName='mumbai',
				   UserData=userDataCode,
                                   InstanceType='t2.micro',
                                   NetworkInterfaces=[
                                       {
                                           'SubnetId': response.id,
                                           'Groups':  [pubSecGrp.id],
                                           'DeviceIndex': 0,
                                           'DeleteOnTermination': True,
                                           'AssociatePublicIpAddress': True,
                                       }
                                   ]
                                   )
vpc_cli.get_waiter('instance_running')
print instance

