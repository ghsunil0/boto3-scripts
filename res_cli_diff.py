import boto3
""" This code shows the difference
    between using the service console as a resource
       or   using the service console as a client
   Note : The resource are only for specific services s3, ec2, cloudformation..
          for other services you can use only client    
"""

aws_man_con=boto3.session.Session(profile_name='sunil-admin')
iam_con_resource=aws_man_con.resource("iam")


for each_user in iam_con_resource.users.all():
    print("user : ", each_user.name)


iam_con_client=aws_man_con.client("iam")
for usr_name in (iam_con_client.list_users()['Users']):
    print ("User :", usr_name['UserName'], " Created : ", usr_name['CreateDate']
           )
