import boto3
import os
from datetime import datetime
from heapq import nlargest

import sys

# Get the zip file name from the command line argument
zip_file_name = sys.argv[1]


# Set your AWS credentials
access_key = 'YOURKEYHERE'
secret_key = 'YOURSECRETHERE'
region = 'YOURREGION'


try:
    # Set your S3 bucket name
    bucket_name = 'YOURBUCKET'

    # Set the local file path to upload
    local_file_path = zip_file_name

    # Set the destination folder in S3
    s3_destination_folder = 'YOURFOLDER'

    # Initialize the S3 client with your credentials
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name=region)

    # Upload file to S3
    s3.upload_file(local_file_path, bucket_name, s3_destination_folder + os.path.basename(local_file_path))

    #   List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=s3_destination_folder)

    # Extract last modified timestamps of objects
    timestamps = [(obj['LastModified'], obj['Key']) for obj in response.get('Contents', [])]

    # Find the oldest files and delete them if there are more than 4 files
    #if len(timestamps) > 4:
     #   oldest_files = nlargest(len(timestamps) - 4, timestamps)
      #  for timestamp, key in oldest_files:
       #     s3.delete_object(Bucket=bucket_name, Key=key)
        #    print(f'Deleted {key}')

except Exception as e:
    # Log the error message to a file
    with open("error_log.txt", "a") as log_file:
        log_file.write(str(e) + "\n")
