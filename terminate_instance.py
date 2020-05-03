import boto3
import pprint

session=boto3.Session(profile_name="default")
ec2_re=session.client(service_name="ec2",region_name="ap-south-1")
instance=ec2_re.terminate_instances(InstanceIds=['i-061e8351e64a6076a'])
print instance

