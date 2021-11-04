""" this is a multi line comment - this is not actual comment
    but a multi line text being used as comment lines
    this will work as a string stored in the code"
"""
# script to get account Id

import boto3

# create management console access 
aws_man_con=boto3.session.Session(profile_name="sunil-admin")

# sts console using client 
sts_con_cli=aws_man_con.client(service_name='sts', region_name='us-east-2')

# List all iam users using client object

response = sts_con_cli.get_caller_identity()

print ("Account id : ", response['Account'])
print ("Arn        : ", response['Arn'])

# or

print ("Account id : ", response.get('Account'))
print ("Arn        : ", response.get('Arn'))

