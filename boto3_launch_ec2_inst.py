import boto3
# File Name : boto3_launch_ec2_inst.py
#
#  This python program will launch ec2 instance
#    in default vpc and any subnet within the revion.
#

aws_man_con_admin=boto3.session.Session(profile_name="sunil-admin")
aws_man_con_ec2  =boto3.session.Session(profile_name='ec2-developer')

# ec2 console with resources and client

ec2_con_res=aws_man_con_admin.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=aws_man_con_admin.client  (service_name='ec2', region_name='us-east-2')


# ami-0f19d220602031aed


resp = ec2_con_cli.run_instances(ImageId='ami-0f19d220602031aed',
         InstanceType='t2.micro',
         MinCount=1,
         MaxCount=1)


for inst_id in resp['Instances']:
    print(inst_id['InstanceId'])
    ec2_id=inst_id['InstanceId']
    print ("instance is created and starting ",ec2_id)
    
    waiter=ec2_con_cli.get_waiter('instance_running')
    waiter.wait(InstanceIds=[ec2_id]) #40 checks after every 15 sec
    print("Now your ec2 instace is up and running")
                      
