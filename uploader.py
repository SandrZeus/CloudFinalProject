import os
import boto3

s3 = boto3.client('s3')

files_path = r'./mockfiles'
# bucket_name = 'awsexample' # Replace with your bucket name

def upload_file_to_s3(file_path, bucket_name, file_key):
    with open(file_path, 'rb') as f:
        s3.upload_fileobj(f, bucket_name, file_key)

def upload_folders_to_s3(base_path, bucket_name):
    for root, dirs, files in os.walk(base_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            relative_path = os.path.relpath(file_path, base_path)
            
            s3_file_key = os.path.join(relative_path.replace(os.path.sep, '/'))

            upload_file_to_s3(file_path, bucket_name, s3_file_key)

# upload_folders_to_s3(files_path, bucket_name) || Correct way to call the function with correct bucket name
