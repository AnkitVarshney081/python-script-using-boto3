import boto3
import pprint

session=boto3.Session(profile_name="default",region_name='ap-south-1')
client=session.client(service_name='ec2')
sec_grp=client.describe_security_groups()
#pprint.pprint(sec_grp['SecurityGroups'])
for each in sec_grp['SecurityGroups']:
	print(each['GroupId'],each['IpPermissions'])
