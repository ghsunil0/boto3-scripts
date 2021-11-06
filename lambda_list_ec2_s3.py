import boto3
#
# Lambda function to display instances and s3 buckets
#
def lambda_handler(event, context):
#
#    aws_man_con=boto3.session.Session(aws_access_key_id="AKI.....", aws_secret_access_key="jKPbQ......../")
#    ec2_con_re=aws_man_con.resource(service_name='ec2', region_name='us-east-2')
#
#    Once role is assigned to the lambda function you can directly 
#    create a connection as follows 
    ec2_con_re=boto3.resource(service_name='ec2', region_name='us-east-2')
    for each_in in ec2_con_re.instances.all():     
        print (each_in.instance_id, each_in.instance_type)
    
    s3_con_re=boto3.resource(service_name='s3', region_name='us-east-2')
    for each_bu in s3_con_re.buckets.all():     
        print (each_bu.name)
    
