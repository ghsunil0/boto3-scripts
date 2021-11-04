import boto3
import csv
from   pprint import pprint

man_con_ec2_dev=boto3.session.Session(profile_name='ec2-developer')

ec2_con_res=man_con_ec2_dev.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=man_con_ec2_dev.client  (service_name='ec2', region_name='us-east-2')

cnt=1

# open csv file in write mode
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)

#create header row
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])


for each in ec2_con_res.instances.all():
#    print ("Count = {} Instance = {} ".format(cnt, each))
        print(cnt,
          each.instance_id,
          each.instance_type,
          each.architecture,
          each.launch_time.strftime("%Y-%m-%d"),
          each.private_ip_address)
        csv_w.writerow([cnt,
          each.instance_id,
          each.instance_type,
          each.architecture,
          each.launch_time.strftime("%Y-%m-%d"),
          each.private_ip_address])
        cnt+=1

                                    
csv_ob.close()

"""
import boto3
import csv
aws_mag_con=boto3.session.Session(profile_name="ec2_developer")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
cnt=1
csv_ob=open("inventory_info.csv","w",newline='')
csv_w=csv.writer(csv_ob)
csv_w.writerow(["S_NO","Instance_Id",'Instance_Type','Architecture','LaunchTime','Privat_Ip'])
for each in ec2_con_re.instances.all():
	print(cnt,each,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address)
	csv_w.writerow([cnt,each.instance_id,each.instance_type,each.architecture,each.launch_time.strftime("%Y-%m-%d"),each.private_ip_address])

    cnt+=1

csv_ob.close()
"""
