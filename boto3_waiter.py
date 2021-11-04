import boto3
import sys
from pprint import pprint
import time


# create management console access
aws_man_con_admin=boto3.session.Session(profile_name="sunil-admin")
aws_man_con_ec2  =boto3.session.Session(profile_name="ec2-developer")

# ec2 console with resources and client

ec2_con_res=aws_man_con_ec2.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=aws_man_con_ec2.client  (service_name='ec2', region_name='us-east-2')


'''
#    The below code is to use the waiter
#    with resource console

my_inst_ob=ec2_con_res.Instance("i-057c181758d1e2547")
print("Starting given instance....")
my_inst_ob.start()
my_inst_ob.wait_until_running()  #Resource waiter waits for 200sec(40 checks after every 5 sec)
print("Now your instance is up and running")
'''

print("Starting ec2 instace...")
ec2_con_cli.start_instances(InstanceIds=['i-057c181758d1e2547'])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f']) #40 checks after every 15 sec
print("Now your ec2 instace is up and running")


'''
my_inst_ob=ec2_con_res.Instance("i-057c181758d1e2547")
print("Starting given instance....")
my_inst_ob.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-002d4110f1199166f'])
print("Now your ec2 instace is up and running")
'''


