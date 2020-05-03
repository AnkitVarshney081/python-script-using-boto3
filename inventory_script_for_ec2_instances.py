import boto3
import csv
from pprint import pprint
session=boto3.Session(profile_name="default")
ec2_re=session.resource(service_name="ec2",region_name="ap-south-1")
header_csv=['S_No','InstanceId','Instance_Type','Instance_Arch','Instance_Public_Ip_Address','Instance_Private_Ip_Address']
S_No=1
fo=open("ec2_inv.csv","wb")
csv_w=csv.writer(fo)
csv_w.writerow(header_csv)
for each_in in ec2_re.instances.all():
	In_Id=each_in.instance_id
	In_Type=each_in.instance_type
	In_Arc=each_in.architecture
	In_Ip=each_in.public_ip_address
	In_pIp=each_in.private_ip_address
	print(S_No,In_Id,In_Type,In_Arc,In_Ip,In_pIp)
	csv_w.writerow([S_No,In_Id,In_Type,In_Arc,In_Ip,In_pIp])
	S_No=S_No+1
fo.close()
