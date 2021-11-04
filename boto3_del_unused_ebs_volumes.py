import boto3
from   pprint import pprint
import csv

# Create Management Console Connection
man_con_admin  =boto3.session.Session(profile_name='sunil-admin')
man_con_ec2_dev=boto3.session.Session(profile_name='ec2-developer')

# create ec2-console for resource and client

ec2_con_res=man_con_ec2_dev.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=man_con_ec2_dev.client  (service_name='ec2', region_name='us-east-2')

# Syntex for filter    filt_unused={"Name":"", "Values":[]}


"""
#
# This code is to delete using service resource
#
filt_unused={"Name":"status", "Values":['available']}

# for each_vol in ec2_con_res.volumes.all():
# for each_vol in ec2_con_res.volumes.limit(3):
for each_vol in (ec2_con_res.volumes.  filter(Filters=[filt_unused])):
    if not each_vol.tags:    # unused and untaged volumes 
        print (each_vol.id, each_vol.state,each_vol.tags)
        print ("Deleting unused and untagged volumes")
        each_vol.delete()

print ("Deleted all unused and untaged volumes" )

"""

# 
# This code is to delete using service client
#  doing the same thing as above but using the client connection
#


for each_vol in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_vol and each_vol['State']=='available':
        print ("Deleting Volume : ", each_vol['VolumeId'], each_vol['State'])
        ec2_con_cli.delete_volume(VolumeId=each_vol['VolumeId'])

print ("All unused and untagged volumes are deleted")

























