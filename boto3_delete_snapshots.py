import boto3
from   pprint import pprint

aws_man_con=boto3.session.Session(profile_name='sunil-admin')

ec2_con_res=aws_man_con.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=aws_man_con.client  (service_name='ec2', region_name='us-east-2')
sts_con_cli=aws_man_con.client  (service_name='sts', region_name='us-east-2')

# format for filter filt_1 = filter("Name":"", "Values"=[])

response=sts_con_cli.get_caller_identity()
my_acc_id=response.get('Account')

for each_snap in ec2_con_res.snapshots.filter(OwnerIds=[my_acc_id]):
   print ("Deleting Snapshot : ", each_snap.id)
   ss_id=each_snap.id
   ret_ans=ec2_con_cli.delete_snapshot(SnapshotId=ss_id)
