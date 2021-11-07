import json
import boto3

def lambda_handler(event, context):
#
#    File : boto3_lambda_for_sshot_all_regions

#           This program to be copied to create a lambda function
#
#   It will create a list of all regions using the meta data for resource
#       to get to client object details
#
#    Some times you may want to access client objects from the
#    resource (not client session)
#    eg : client.describe_region() to get the region ids
#    in that case you can use resource meta objects resource.meta
#    in resource.meta you have client object as resource.meta.client
#    and that's way to get to client objects
#    resource.meta.client.describe_region()['Region'] - collection
#    for each resource.meta.client.describe_region()['Region'] for each region
#
#



# define management console sessions for admin and ec2-developer

#    man_con_admin   =boto3.session.Session(profile_name='sunil-admin')
#    man_con_ec2_dev =boto3.session.Session(profile_name='ec2-developer')

# define ec2 console for resource and client

    ec2_dev_con_res = boto3.resource(service_name='ec2')
    ec2_dev_con_cli = boto3.client  (service_name='ec2')

    all_regions=[]
    for each_obj in (ec2_dev_con_res.meta.client.describe_regions()['Regions']):
#        print ("Region Name : {} ".format(each_obj['RegionName']))
        all_regions.append(each_obj['RegionName'])

#   print (all_regions)

    for each_region in all_regions:
        print ("Working on Region {}".format(each_region))
        ec2_con_cli = boto3.client  (service_name='ec2',region_name=each_region)

        f_dev_bak={"Name":"tag:Dev","Values":['Backup']}

        list_all_vol_ids=[]
        for each_vol in  (ec2_con_cli.describe_volumes(Filters=[f_dev_bak])['Volumes']):
            list_all_vol_ids.append(each_vol['VolumeId'])

        print (list_all_vol_ids)
        print ("Start of paginate logic")
        if bool(list_all_vol_ids)==False:
            print ("Skipping Region = ",each_region)
            print ("============================")
            continue


        list_all_vol_ids=[]
        allpages=ec2_con_cli.get_paginator('describe_volumes')
        for each_page in (allpages.paginate(Filters=[f_dev_bak])):
#           pprint (each_page)
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

    


