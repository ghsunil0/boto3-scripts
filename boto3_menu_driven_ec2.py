import boto3
import sys
from pprint import pprint



# create management console access
aws_man_con_admin=boto3.session.Session(profile_name="sunil-admin")
aws_man_con_ec2  =boto3.session.Session(profile_name='ec2-developer')

# ec2 console with resources and client

ec2_con_res=aws_man_con_ec2.resource(service_name='ec2', region_name='us-east-2')
ec2_con_cli=aws_man_con_ec2.client  (service_name='ec2', region_name='us-east-2')


while True:
    print ("This script performs the following actions on ec2 instance")
    print ("""
        1. Start
        2. Stop
        3. Terminate
        4. Exit
        """)
    opt=int(input("Enter your option 1 to 4 :  "))
    if opt==1:
        instance_id=input("Enter your instance id : ")
        my_curr_ec2=ec2_con_res.Instance(instance_id)
        # pprint(dir(my_curr_ec2))
        print ("Starting     ect instance ......", instance_id)
     
        # Using resource for single instance 
        # my_curr_ec2.start()
        
        # Using Client for multiple instances
        ec2_con_cli.start_instances(InstanceIds=[instance_id])
    elif opt==2:
        instance_id=input("Enter your instance id : ") 
        my_curr_ec2=ec2_con_res.Instance(instance_id)
        print ("Stopping    ect instance ......", instance_id)
        
        # Using resource for single instance 
        # my_curr_ec2.stop()

        # Using Client for multiple instances
        ec2_con_cli.stop_instances(InstanceIds=[instance_id])
    elif opt==3:
        instance_id=input("Enter your instance id : ") 
        my_curr_ec2=ec2_con_res.Instance(instance_id)
        print ("Terminating    ect instance ......", instance_id)
        
        # Using resource for single instance 
        # my_curr_ec2.terminate()
        
        # Using Client for multiple instances
        ec2_con_cli.terminate_instances(InstanceIds=[instance_id])
        
    elif opt==4:
        print("Thanks you for using this script" )
        sys.exit()
    else:
        print ("Invalid Option - Enter 1,2,3,4 " )
    
        
               
