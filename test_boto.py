import boto3
""" this is a multi line comment - this is not actual comment
    but a multi line text being used as comment lines
    this will work as a string stored in the code"
"""


aws_man_con=boto3.session.Session(profile_name="sunil-admin")
ec2=aws_man_con.resource("ec2")

iam_con=aws_man_con.resource('iam')

for each_user in iam_con.users.all():
    print ("user : ", each_user.name)


aws_man_con=boto3.session.Session(profile_name="s3-dev")
s3_con=aws_man_con.resource('s3')
for each_buk in s3_con.buckets.all():
    print ("bucket : ", each_buk.name)
  
