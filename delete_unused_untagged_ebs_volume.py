import boto3
import csv
from pprint import pprint
session=boto3.Session(profile_name="default")
ec2_re=session.resource(service_name="ec2",region_name="ap-south-1")
ec2_cli=session.client(service_name="ec2",region_name="ap-south-1")
all_required_volume_ids=[]
for each_vol in ec2_re.volumes.all():
	if each_vol.state=="available" and each_vol.tags==None:
		print each_vol.id,each_vol.state,each_vol.tags
		all_required_volume_ids.append(each_vol.id)
		each_vol.delete()
                
waiter = ec2_cli.get_waiter('volume_deleted')
try:
	waiter.wait(VolumeIds=all_required_volume_ids)
	print "Successfully deleted all your volumes which are unused and untagged EBS volume"
except Exception as e:
	print e
#for each_vol in ec2_re.volumes.all():
#	pprint( dir(each_vol))
	#break
