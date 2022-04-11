from email.policy import Policy
import boto3
import os
from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile
import json
import requests
import mimetypes


# CREATE BUCKET
s3 = boto3.client("s3")
bucket_name = "martapalermolab1"
s3.create_bucket(Bucket = bucket_name)


# DOWNLOAD AND UNZIP FILES FROM STATIC WEBSITE URL
url = 'https://github.com/martapalermo/martapalermo.github.io/archive/refs/heads/main.zip'

# download the file by sending request to url 
req = requests.get(url)
print('Downloading Completed')


# extract zip file contents 
zipfile = ZipFile(BytesIO(req.content))
zipfile.extractall('.')

# loop in folder to access all files
for root, dirs, files in os.walk("martapalermo.github.io-main"):
    for file in files:
        full_path = os.path.join(root, file)
        print(full_path)
        key = full_path[len('martapalermo.github.io-main/'):]
        obj = mimetypes.guess_type(key)
        content_type = obj[0]
        if content_type is None:
            s3.put_object(Bucket = 'martapalermolab1', Key = key, Body = open(full_path, 'rb'))
        else:
            s3.put_object(Bucket = 'martapalermolab1', Key = key, Body = open(full_path, 'rb'), ContentType = content_type)


# define and set configuration 
website_configuration = {
        'IndexDocument': {'Suffix': 'index.html'}
}

s3 = boto3.client('s3')
s3.put_bucket_website(Bucket = 'martapalermolab1', WebsiteConfiguration = website_configuration)

# Setting bucket policy 
    # create new policy
bucket_name = 'martapalermolab1'
bucket_policy = {
            'Version': '2012-10-17',
            'Statement': [{
                'Sid': 'AddPermission',
                'Effect': 'Allow',
                'Principal': '*',
                'Action': ['s3:GetObject'],
                'Resource': f'arn:aws:s3:::martapalermolab1/*'
             }]
 }

bucket_policy = json.dumps(bucket_policy)

    # set the new policy created
s3 = boto3.client('s3')
s3.put_bucket_policy(Bucket = bucket_name, Policy = bucket_policy)
