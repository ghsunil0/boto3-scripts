import boto3

from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

def create_table():
    dynamodb = boto3.resource('dynamodb')

 
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
            ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            }],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
            }
        )
    print("Table status:", table.table_status)


# create_table()

def get_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users')      
    resp = table.get_item(
            Key={
                'id' : 2,
                }
            )
                
    if 'Item' in resp:
        print(resp['Item'])


'''
    for xid in [2, 4, 3 ]:
        resp = table.get_item(
                Key={
                    'id' : xid
                }
            )
        print ("="*20)
        if 'Item' in resp:
            print(resp['Item'])
        else :
            print ("User {} not found".format(xid))
            
resp = table.get_item(
        Key={
            'id' : 2,
            }
            )
                
    if 'Item' in resp:
        print(resp['Item'])
'''
    #{'email': 'sam0_2000@hotmail.com', 'id': Decimal('2'), 'fname': 'Sunil', 'sname': 'Thakkar'}
    #{'email': 'avi_t@hotmail.com',     'id': Decimal('3'), 'fname': 'Avi',   'sname': 'Thakkar'}

def query_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users')      

    xid = 1     
    resp = table.query(
        KeyConditionExpression=Key('id').eq(xid)
    )

    print ("==== query id = 1 =====")                
    if 'Item' in resp:
        print(resp['Item'][0])
    else:
        print ("User {} not found".format(xid))
    print ("==== query =====")                
  
    xid = 2     
    resp = table.query(
        KeyConditionExpression=Key('id').eq(xid)
    )

    print ("==== query id = 2 =====")                
    if 'Items' in resp:
        print(resp['Items'][0])
    else:
        print ("User {} not found".format(xid))
    print ("==== query =====")                
    #{'email': 'sam0_2000@hotmail.com', 'id': Decimal('2'), 'fname': 'Sunil', 'sname': 'Thakkar'}
    #{'email': 'avi_t@hotmail.com',     'id': Decimal('3'), 'fname': 'Avi',   'sname': 'Thakkar'}
  

def update_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users')
    
    table.update_item(
        Key={
                'id': 2,
            },
        UpdateExpression="set fname = :g",
        ExpressionAttributeValues={
                ':g': "Sunil-Updated"
            },
        ReturnValues="UPDATED_NEW"
        )
        
    get_item()
    
    #{'email': 'sam0_2000@hotmail.com', 'id': Decimal('2'), 'fname': 'Sunil', 'sname': 'Thakkar'}
    #{'email': 'avi_t@hotmail.com',     'id': Decimal('3'), 'fname': 'Avi',   'sname': 'Thakkar'}

def delete_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users')
    
    response = table.delete_item(
        Key={
            'id': 3,
        },
    )
    #{'email': 'sam0_2000@hotmail.com', 'id': Decimal('2'), 'fname': 'Sunil', 'sname': 'Thakkar'}
    #{'email': 'avi_t@hotmail.com',     'id': Decimal('3'), 'fname': 'Avi',   'sname': 'Thakkar'}

def create_bunch_of_users():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('users') 
    
    for n in range(10):
        table.put_item(Item={
            'id': n,
            'fname': 'Sunil',
            'lname': 'Thakkar' + str(n),
            'email': 'sam0_2000'+ str(n) +'@test.com'
        })

# create_table()
# get_item()
# query_item()
# update_item()
# delete_item()
create_bunch_of_users()

