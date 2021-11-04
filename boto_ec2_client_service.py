"""
    Script to test some of the
    possibilities with ec2 services
"""

# script to get account Id

import boto3
from pprint import pprint


# create management console access
aws_man_con_admin=boto3.session.Session(profile_name="sunil-admin")
aws_man_con_ec2  =boto3.session.Session(profile_name='ec2-developer')

# ec2 console with resources and client

ec2_con_res=aws_man_con_ec2.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=aws_man_con_ec2.client  (service_name='ec2', region_name='us-east-2')

# List all iam users using client object
response = ec2_con_cli.describe_instances()['Reservations']

print ("=======================")
for each_item in response:
    for each in each_item['Instances']:
        print ("The image ID is : {}\nThe Instance ID is {}\nThe Instance Launc Time is : {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))
        print ("=======================")

response = ec2_con_cli.describe_volumes()['Volumes']
for each in response:
    print ("The Volume ID is : {}\n Type is {} Size is {}\nVolume State : {}".format(each['VolumeId'],each['VolumeType'],each['Size'],each['State']))
    print ("=======================")

'''

for each_item in response:
    for each in each_item['Instances']:
        print("The image ID is : {}\nThe Instance ID is {}\nThe Instance Launc Time is : {}".format(each['ImageId'],each['InstanceId'],each['LaunchTime'].strftime("%Y-%m-%d")))
        print "======================="
'''











'''
print ("Account id : ", response['Account'])
print ("Arn        : ", response['Arn'])

# or

print ("Account id : ", response.get('Account'))
print ("Arn        : ", response.get('Arn'))
'''


