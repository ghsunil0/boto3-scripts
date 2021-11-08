import json
import boto3

# Lambda Function : lambda_s3_to_dynamodb 
# Develiper       : Sunil Thakkar
# Details         :
#    This script will be triggered whenever a employee csv file will be uploaded 
#        to a specific bucket
#        The script will read all the employee records from the csv file  
#        and load the records to dynamod db employee table
#        TOTO
#        once the records are loaded 
#                 the file will be moved to completed bucket 
#                 and email will be sent to the managers with the status email
#
#  
#
# 
def lambda_handler(event, context):
    s3_client = boto3.client('s3')    # This will use the default profile
    bucket_name =event['Records'][0]['s3']['bucket']['name']
    s3_file_name=event['Records'][0]['s3']['object']['key']

#    print (bucket_name)
#    print (s3_file_name)

    resp     = s3_client.get_object(Bucket=bucket_name, Key = s3_file_name)
    data     = resp['Body'].read().decode('utf-8')
    employees= data.split("\n")
    DyDb     = boto3.resource('dynamodb')
    table    = DyDb.Table('employees')
#    print (employees)
    
    for emp in (employees):
        if len(emp) ==0:
            continue
        
        emp_data=emp.split(",")
        emp_id   = int(emp_data[0])
        emp_name = emp_data[1]
        emp_loc  = emp_data[2]
 #       print ("="*20)
 #       print (emp)
 #       print (emp_id)
 #       print (emp_name)
 #       print (emp_loc)
        try:
            table.put_item(
                Item = {
                    "emp_id"   : emp_id,
                    "emp_name" : emp_name,
                    "emp_loc"  : emp_loc}
                )
        except Exception as e:
            print(e)
            







'''
