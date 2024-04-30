import boto3
import os
import csv
import json
from io import StringIO

s3 = boto3.client('s3')
sns = boto3.client('sns')

S3_BUCKET = os.environ['s3_bucket']
TOPIC_ARN = os.environ['sns_topic']


def lambda_handler(event, context):
    print(event['Records'][0])

    event_name = event['Records'][0]['eventName']
    # bucket = event['Records'][0]['s3']['bucket']['name']
    bucket = S3_BUCKET
    key = event['Records'][0]['s3']['object']['key']
    print(f"bucket name: {bucket} - file name: {key}")

    response = s3.get_object(Bucket=bucket, Key=key)

    if response:
        data = response['Body'].read().decode('utf-8')
        emails = process_data(data)
        if emails:
            sns_response = send_notification(key, bucket, emails)
            if sns_response:
                print("SNS publish successful")
            else:
                print("SNS publish failed")
        else:
            print("No enails found in the CSV")
    else:
        print("Get Object - failed")


def process_data(data):
    file = StringIO(data)
    reader = csv.reader(file, delimiter=',')
    emails = {}
    next(reader)
    for item in reader:
        if item:
            emails[f"{item[1]} {item[2]}"] = item[3]
    return emails


def send_notification(key, bucket, emails):
    sns_message = json.dumps(emails, indent=2)
    subject = f"Object uploaded into the {S3_BUCKET} bucket."
    sns_response = sns.publish(
        TargetArn=TOPIC_ARN,
        Message=sns_message,
        Subject=subject
    )
    return sns_response
