import os
import boto3
from botocore.exceptions import NoCredentialsError

def upload_folder_to_s3(local_folder_path, s3_bucket_name):
    s3 = boto3.client('s3')

    try:
        for root, dirs, files in os.walk(local_folder_path):
            for file in files:
                local_file_path = os.path.join(root, file)
                s3_file_key = os.path.relpath(local_file_path, local_folder_path).replace(os.sep, "/")
                s3.upload_file(local_file_path, s3_bucket_name, s3_file_key)

        s3_bucket_link = f'https://{s3_bucket_name}.s3.amazonaws.com/'
        return s3_bucket_link

    except NoCredentialsError:
        print("Credentials not available")

def download_file_from_s3(s3_bucket_name, s3_file_key, local_download_path):
    s3 = boto3.client('s3')

    try:
        s3.download_file(s3_bucket_name, s3_file_key, local_download_path)
        print(f"File downloaded to {local_download_path}")

    except NoCredentialsError:
        print("Credentials not available")

local_folder_to_upload = r'Users\sandr\OneDrive\Desktop\Memes'
s3_bucket_name = 'sandro-keonho-bucket-a'

folder_link = upload_folder_to_s3(local_folder_to_upload, s3_bucket_name)
print(f"Folder uploaded to S3. Folder link: {folder_link}")

s3_file_key_to_download = 'path/within/bucket/to/file.txt'
local_download_path = '/path/to/local/download/file.txt'

download_file_from_s3(s3_bucket_name, s3_file_key_to_download, local_download_path)
