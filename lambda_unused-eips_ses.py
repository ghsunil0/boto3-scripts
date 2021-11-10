import boto3
import os

ec2_client = boto3.client('ec2')
ses_client = boto3.client('ses')


# the import os is required to access the environment variables
# The environment variables for lambda function will
# in the configuration section environment variables
# 
SOURCE_EMAIL = os.environ['SOURCE_EMAIL']
DEST_EMAIL   = os.environ['DEST_EMAIL']

def lambda_handler(event,context):
    response = ec2_client.describe_addresses()
    unused_eips = []
    for address in response['Addresses']:
        if 'InstanceId' not in address  :
            unused_eips.append(address['PublicIp'])

    # send email using ses
    # SES should have the email addresses as already varified address 
    sesClient.send_email(
           Source = SOURCE_EMAIL,
           Destination={
            'ToAddresses': [
                DEST_EMAIL
            ]
          },
          Message={
            'Subject': {
                'Data': 'Unused  EIPS',
                'Charset': 'utf-8'
            },
            'Body': {
                'Text': {
                    'Data': str(eips),
                    'Charset': 'utf-8'
                }
            }
          }
        )
        
