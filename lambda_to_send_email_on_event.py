import boto3
# File Name : lambda_to_send_email.py
#
# This Lambda function will send an email  
#  The email will take the status of a particular instance 
#  that is being monitored by the EventBridge event.
#  
#  This lambda function will be called when the monitored event
#    changes the state to stopped (Event change is in the EventBridge Event) 
#   
#  Needs to be changed so it will take instance-id as parameter
#

def lambda_handler(event, context):

    ec2_con_res=boto3.resource(service_name='ec2', region_name='us-east-2')
    sns_con_cli=boto3.client  (service_name='sns', region_name='us-east-2')
    my_inst=ec2_con_res.Instance('i-057c181758d1e2547')    
    msg="Production instance is "+my_inst.state['Name']
#    print(msg)
    
    sns_con_cli.publish(TargetArn='arn:aws:sns:us-east-2:860479642281:send_email',
                        Subject=msg,
                        Message=msg)
