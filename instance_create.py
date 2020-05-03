import boto3
ec2=boto3.resource('ec2','ap-south-1')
instance = ec2.create_instances(ImageId='ami-0470e33cd681b2476',MinCount=1,MaxCount=1,InstanceType='t2.micro')
print instance[0].id
