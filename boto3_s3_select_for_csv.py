import boto3

s3_client = boto3.client('s3')

resp = s3_client.select_object_content(
    Bucket='emp-to-dynamodb',
    Key='employee_det.csv',
    Expression='select e.emp_id, e.emp_name, e.emp_loc, e.emp_age from S3Object e',
    ExpressionType='SQL',
    
    InputSerialization ={'CSV': { 'FileHeaderInfo': 'USE'}} ,
    OutputSerialization={'CSV': {}},
#    ScanRange={'Start': 1, 'End': 4}
    )

# loop through the resp object

for each_rec in resp['Payload']:
    if 'Records' in each_rec:
        print (each_rec['Records']['Payload'].decode())


'''
responce is Dict : List of Payloads :
{
    'Payload': EventStream({
        'Records': {
            'Payload': b'bytes'
        },
}

response = client.select_object_content(
    Bucket='string',
    Key='string',
    SSECustomerAlgorithm='string',
    SSECustomerKey='string',
    Expression='string',
    ExpressionType='SQL',
    RequestProgress={
        'Enabled': True|False
    },
    InputSerialization={
        'CSV': {
            'FileHeaderInfo': 'USE'|'IGNORE'|'NONE',
            'Comments': 'string',
            'QuoteEscapeCharacter': 'string',
            'RecordDelimiter': 'string',
            'FieldDelimiter': 'string',
            'QuoteCharacter': 'string',
            'AllowQuotedRecordDelimiter': True|False
        },
        'CompressionType': 'NONE'|'GZIP'|'BZIP2',
        'JSON': {
            'Type': 'DOCUMENT'|'LINES'
        },
        'Parquet': {}

    },
    OutputSerialization={
        'CSV': {
            'QuoteFields': 'ALWAYS'|'ASNEEDED',
            'QuoteEscapeCharacter': 'string',
            'RecordDelimiter': 'string',
            'FieldDelimiter': 'string',
            'QuoteCharacter': 'string'
        },
        'JSON': {
            'RecordDelimiter': 'string'
        }
    },
    ScanRange={
        'Start': 123,
        'End': 123
    },
    ExpectedBucketOwner='string'
)


'''
