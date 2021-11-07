import boto3
from   pprint import pprint
# File Name : lambda_to_automate_snapshot.py
#
# This Lambda function will generate a list of volumes
#      for which snap-shot needs to be taken
#      and will create the snap-shot on a schedule
#
#      It will build a list of snapsshot_ids
#         and the waiter will wait till all the snapshots are completed
#
#      The lambda function will be triggred on schedule
#          by EventBridge scheduled event
#
#  This will use client.descrribe.volume() to list volumes



aws_man_con=boto3.session.Session(profile_name='sunil-admin')
iam_con_cli=aws_man_con.client(service_name='iam', region_name='us-east-2')
ec2_con_cli=aws_man_con.client(service_name='ec2', region_name='us-east-2')

# pprint (ec2_con_cli.describe_volumes()['Volumes'])
#filt_dev_backup={"Name":"","Values"[]}
f_dev_bak={"Name":"tag:Dev","Values":['Backup']}

list_all_vol_ids=[]
for each_vol in  (ec2_con_cli.describe_volumes(Filters=[f_dev_bak])['Volumes']):
    list_all_vol_ids.append(each_vol['VolumeId'])

print (list_all_vol_ids)
print ("Start of paginate logic")


list_all_vol_ids=[]
allpages=ec2_con_cli.get_paginator('describe_volumes')
for each_page in (allpages.paginate(Filters=[f_dev_bak])):
#    pprint (each_page)
    for each_vol in each_page['Volumes']:
        list_all_vol_ids.append(each_vol['VolumeId'])

print (list_all_vol_ids)

print ("======================")
snaps_ids=[]
for each_vol_id in list_all_vol_ids:
    print ("Taking SnapShot for Volume id :{}".format(each_vol_id))
    res=ec2_con_cli.create_snapshot(
                Description="Taking snap shot with Lambda via EventBridge",
                VolumeId=each_vol_id,
                TagSpecifications=
                   [
                    {'ResourceType':'snapshot',
                     'Tags' : [
                         {
                             'Key'  : 'Delete-on',
                             'Value' : '90'
                        }
                              ]
                    }
                    ]
                )
    snaps_ids.append(res.get('SnapshotId'))

print (snaps_ids)

waiter = ec2_con_cli.get_waiter('snapshot_completed')
waiter.wait(SnapshotIds=snaps_ids)

print ("Successfully completed snaps for the volume of {}".format(snaps_ids))

    
'''
for each_page in allpages.paginate():   # this will give 1 page of list of users 
    for each_obj in each_page['Users']:         # this will be each user from the list
        cnt=cnt+1
        print (cnt, " ", each_user['UserName'])
'''
