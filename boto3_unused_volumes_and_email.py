import boto3
#
# program : boto3_unused_volumes_and_email.py
#
# This program will find all the volumes that
# are not attached and will send a email
# via sns notifications.
#
# This will use describe_volumes() to get all the volumes
#   for each volume it will check if any assignments are there
#      (if no attachements then the length of the attachements will be 0
# You need to have a sns topic and everyone
#   subscribed to that topic will recieve the email
#


ec2_client = boto3.client('ec2')    # This will use the default profile
sns_client = boto3.client('sns')    # This will use the default profile

sns_arn = 'arn:aws:sns:us-east-2:860479642281:send_email'
volumes = ec2_client.describe_volumes()

vol_size=0
unused_vols = []
for volume in volumes['Volumes']:
    if len(volume['Attachments']) == 0:
        unused_vols.append(volume['VolumeId'])
        vol_size=vol_size + volume['Size']
        print(volume)
        print("="*20)

email_body = "##### Unused Volumes ##### \n"

for vol in unused_vols:
    email_body = email_body + "VolumeId = {} \n".format(vol)

email_body = email_body + "Total unused volume size = {} GB \n".format(vol_size)
# Send Email

sns_client.publish(
    TopicArn = sns_arn,
    Subject = 'Unused Volumes',
    Message = email_body
)
print(email_body)
