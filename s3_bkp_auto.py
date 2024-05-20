import boto3
import os
from datetime import datetime, timedelta

# AWS credentials and region
aws_access_key_id = 'YOURACCESSKEY HERE'
aws_secret_access_key = 'YOURSECRETKEYHERE'
aws_region = 'YOURREGIONHERE'

# S3 bucket and folder
bucket_name = 'YOURBUCKETHERE'
folder_name = 'YOURFOLDERHERE'

# Local backup directory
backup_dir = '/tmp/dbbkp/'

# Upload backup file to S3
def upload_to_s3(file_path, s3_key):
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=aws_region)
    s3.upload_file(file_path, bucket_name, s3_key)

# Delete old backups from S3
def delete_old_backups():
    s3 = boto3.client('s3',
                      aws_access_key_id=aws_access_key_id,
                      aws_secret_access_key=aws_secret_access_key,
                      region_name=aws_region)
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=folder_name+'/backup_')
    if 'Contents' in response:
        backups = sorted(response['Contents'], key=lambda x: x['LastModified'])
        if len(backups) > 4:
            for obj in backups[:-4]:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])

# Main function
def main():
    # Dump MySQL database
    # Replace this with your MySQL dump command or script
    os.system('mysqldump amityacu_amitymoodle > {}/backup_{}.sql'.format(backup_dir, datetime.now().strftime("%Y-%m-%d")))

    # Upload backup file to S3
    upload_to_s3('{}/backup_{}.sql'.format(backup_dir, datetime.now().strftime("%Y-%m-%d")), '{}/backup_{}.sql'.format(folder_name, datetime.now().strftime("%Y-%m-%d")))

    # Delete old backups from S3
    delete_old_backups()

if __name__ == "__main__":
    main()
