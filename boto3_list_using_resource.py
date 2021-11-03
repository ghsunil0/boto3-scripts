import boto3
""" this is a multi line comment - this is not actual comment
    but a multi line text being used as comment lines
    this will work as a string stored in the code"
"""

# create management console access 
aws_man_con=boto3.session.Session(profile_name="sunil-admin")

# iam, ec2 and s3 create uwing client 
iam_con_res=aws_man_con.resource(service_name='iam', region_name='us-east-2')
ec2_con_res=aws_man_con.resource(service_name='ec2', region_name='us-east-2')
s3_con_res =aws_man_con.resource(service_name='s3' , region_name='us-east-2')

# List all iam users using client object

# print all available methods 
# print (dir(iam_con_res.users))
# print (iam_con_res.users.all())

for each_user in iam_con_res.users.limit(3):
    print ("User : ", each_user.name)

#for each_bkt in s3_con_res.buckets.all():
#     print("Bucket : ", each_bkt.name


for each_bkt in s3_con_res.buckets.limit(4):
#    print (dir(each_bkt))
#    break
     print("Bucket : ", each_bkt.name)
           
"""

resp=iam_con_cli.list_users()

for each_user in (resp['Users']):
    print ("User : ", each_user['UserName'])


resp_inst=ec2_con_cli.describe_instances()
inst_count = 0

for inst_det in resp_inst['Reservations']:
    inst_count=inst_count+1
#     print ("Instance details ",inst_count," : ",inst_det['Instances'])
    for inst_id in (inst_det['Instances']):
        print ("Instance id ",inst_count, " : ", inst_id['InstanceId'])

#List all s3 buckets
buck_list=s3_con_cli.list_buckets()
for each_item in buck_list['Buckets']:
	print(each_item['Name'])
	#print(each_item.get('Name'))

"""
