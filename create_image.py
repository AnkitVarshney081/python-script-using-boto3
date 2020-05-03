import boto3
import pprint

session=boto3.Session(profile_name="default")
ec2_client=session.client(service_name="ec2",region_name="ap-south-1")

response = ec2_client.create_image(
    BlockDeviceMappings=[
        {
            'DeviceName':'/dev/xvda',
	    'Ebs': {
	        'DeleteOnTermination': True,
		'VolumeSize': 8,
		'VolumeType': 'gp2',
		'Encrypted' : False
         },
      },
    ],
    Description='Ami for linux machine',
    InstanceId='i-061e8351e64a6076a',
    Name='Ami'
)
