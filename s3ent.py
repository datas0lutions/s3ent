print(r"""

          .d8888b.                    888    
         d88P  Y88b                   888    
              .d88P                   888    
.d8888b      8888"   .d88b.  88888b.  888888 
88K           "Y8b. d8P  Y8b 888 "88b 888    
"Y8888b. 888    888 88888888 888  888 888    
     X88 Y88b  d88P Y8b.     888  888 Y88b.  
 88888P'  "Y8888P"   "Y8888  888  888  "Y888 
 """)                 
                                             
import requests
import boto3
from botocore import UNSIGNED
from botocore.client import Config

s3_client = boto3.client("s3", config=Config(signature_version=UNSIGNED))

def list_objects(bucket, output_file, prefix='', delimiter='', continuation_token=None):
    kwargs = {
        'Bucket': bucket,
        'Prefix': prefix,
        'Delimiter': delimiter,
        'MaxKeys': 100000
    }

    if continuation_token:
        kwargs['ContinuationToken'] = continuation_token

    response = s3_client.list_objects_v2(**kwargs)

    # Write files and folders to the output file
    with open(output_file, 'a') as file:
        for obj in response.get('Contents', []):
            file.write('File: ' + obj['Key'] + '\n')
            print('File:', obj['Key'])

        for common_prefix in response.get('CommonPrefixes', []):
            file.write('Folder: ' + common_prefix['Prefix'] + '\n')
            print('Folder:', common_prefix['Prefix'])
            list_objects(bucket, output_file, prefix=common_prefix['Prefix'], delimiter=delimiter)

    if response['IsTruncated']:
        list_objects(bucket, output_file, prefix=prefix, delimiter=delimiter, continuation_token=response['NextContinuationToken'])


bucket_name = input("Enter Bucket: ")  # Prompting user for bucket name
output_file_name = input("Enter Output File Name: ")  # Prompting user for output file name
prefix = ''

list_objects(bucket_name, output_file_name, prefix=prefix)
