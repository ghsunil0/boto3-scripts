import os,sys

try:
    import boto3
    print("Imported boto3")
except Exception as e:
    print (e)
    sys.exit(1)

source_region='us-east-2'
dest_region  ='us-east-1'
from   pprint import pprint

# File Name : boto3_copy_snapshot_to_oth_region.py
#
# This Lambda function will copy snapshots
#      from us-east-2 to us-east-1
#
#      Filter = snapshots with tag = backup and value = yes
#



aws_man_con=boto3.session.Session(profile_name='sunil-admin')
iam_con_cli=aws_man_con.client(service_name='iam', region_name='us-east-2')
ec2_con_cli=aws_man_con.client(service_name='ec2', region_name='us-east-2')

src_reg='us-east-2'
dst_reg='us-east-1'

ec2_con_src_cli=aws_man_con.client(service_name='ec2', region_name=src_reg)
ec2_con_dst_cli=aws_man_con.client(service_name='ec2', region_name=dst_reg)
sts_con_src_cli=aws_man_con.client(service_name='sts', region_name=src_reg)

account_id=sts_con_src_cli.get_caller_identity().get('Account')
print ("Account ID = {}".format(account_id))

bkp_ss_list=[]
filt_bkp={"Name":"tag:backup","Values":['yes']}
for each_snap in ec2_con_src_cli.describe_snapshots(OwnerIds=[account_id],Filters=[filt_bkp]).get('Snapshots'):
    print ("======================")
    print (each_snap.get('SnapshotId'))
    bkp_ss_list.append(each_snap.get('SnapshotId'))
print (bkp_ss_list)

for each_src_snapid in bkp_ss_list:
    print ("Taking backup for id of {} into {} ".format(each_src_snapid,dst_reg))

    ec2_con_dst_cli.copy_snapshot(
        Description='Disaster Recovery',
        SourceRegion=src_reg,
        SourceSnapshotId=each_src_snapid
        )

print("Snapshot Copy Complete")
print("Modifying tags to completed")

for each_src_snapid in bkp_ss_list:
    ec2_con_src_cli.delete_tags(
        Resources=[each_src_snapid],
        Tags=[ {'Key': 'backup','Value': 'yes'}]
        )

    ec2_con_src_cli.create_tags(
        Resources=[each_src_snapid],
        Tags=[ {'Key': 'backup','Value': 'completed'}]
        )



'''

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

'''
for each_page in allpages.paginate():   # this will give 1 page of list of users 
    for each_obj in each_page['Users']:         # this will be each user from the list
        cnt=cnt+1
        print (cnt, " ", each_user['UserName'])
'''
