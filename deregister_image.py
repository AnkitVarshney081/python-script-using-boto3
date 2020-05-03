import boto3
import pprint

session=boto3.Session(profile_name="default")
ec2_client=session.client(service_name="ec2",region_name="ap-south-1")

response = ec2_client.deregister_image(ImageId="ami-0d35d4f99f8dd3b88")
