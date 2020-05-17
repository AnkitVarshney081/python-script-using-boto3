Boto 3 - The AWS SDK for Python

Build Status Version Gitter

Boto3 is the Amazon Web Services (AWS) Software Development Kit (SDK) for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2. You can find the latest, most up to date, documentation at our doc site, including a list of services that are supported.

Quick Start

First, install the library and set a default region:

$ pip install boto3

Next, set up credentials (in e.g. ~/.aws/credentials):

[default]
aws_access_key_id = YOUR_KEY
aws_secret_access_key = YOUR_SECRET
Then, set up a default region (in e.g. ~/.aws/config):

[default]
region=us-east-1
Then, from a Python interpreter:

>>> import boto3
>>> s3 = boto3.resource('s3')
>>> for bucket in s3.buckets.all():
        print(bucket.name)

Ask a question on Stack Overflow and tag it with boto3
Come join the AWS Python community chat on gitter
Open a support ticket with AWS Support
If it turns out that you may have found a bug, please open an issue
