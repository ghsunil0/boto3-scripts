import boto3
# File Name : lambda_to_stop_ec2_inst.py
#
# This Lambda function will stop all the dev instances 
#  The lambda function needs to be scheduled through eventbridge 
#  Currently scheduled to stop every-week day at 8:00 AM 
#

def lambda_handler(event, context):

    ec2_con_re=boto3.resource(service_name='ec2', region_name='us-east-2')
    dev_ec2_instances={'Name': "Env" , "Values" : ["Dev"]}
    filt_1 = {"Name": "tag:Env", "Values":['Dev']}
    for each_in in ec2_con_re.instances.filter(Filters=[filt_1]):
#        print (each_in.instance_id, each_in.instance_type)
        each_in.stop()

# End of lambda function 

'''
the output for print only

START RequestId: a56c4346-6807-4ede-b440-7b7f155a18a5 Version: $LATEST
i-02ba87a4c0196755a t2.large
i-057c181758d1e2547 t2.micro
END RequestId: a56c4346-6807-4ede-b440-7b7f155a18a5
REPORT RequestId: a56c4346-6807-4ede-b440-7b7f155a18a5	Duration: 876.44 ms	Billed Duration: 877 ms	Memory Size: 128 MB	Max Memory Used: 81 MB
'''
