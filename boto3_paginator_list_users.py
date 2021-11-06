#!/bin/python
import boto3
from   pprint import pprint
iam_man_con=boto3.session.Session(profile_name="sunil-admin")


iam_con_res=iam_man_con.resource(service_name="iam",region_name="us-east-2")
iam_con_cli=iam_man_con.client  (service_name="iam",region_name="us-east-2")


for each_user in iam_con_res.users.all():
    print ("UserName={} UserId={} ".format(each_user.user_name,each_user.user_id))

cnt=0
for each_user in iam_con_cli.list_users()['Users']:
    cnt=cnt+1
    print (cnt, " ", each_user['UserName'])

print ("==========================")
cnt=0
allpages=iam_con_cli.get_paginator('list_users')
for each_page in allpages.paginate():   # this will give 1 page of list of users 
    for each_user in each_page['Users']:         # this will be each user from the list
        cnt=cnt+1
        print (cnt, " ", each_user['UserName'])

print (" Completed all pages ")
print ("==========================")


# similarly to list all ec2 instances using paginator
ec2_con_cli=iam_man_con.client  (service_name="ec2",region_name="us-east-2")
cnt=0
allpages=ec2_con_cli.get_paginator('describe_instances')
for each_page in allpages.paginate():   # this will give 1 page of list of instances
#    pprint (each_page)
    for each_inst in each_page['Instances']:         # this will be each instance from the list
        cnt=cnt+1
        print ("Instance :", cnt, " ", each_inst.InstanceId)
 
#####################
    
