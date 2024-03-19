import boto3
import csv
import os
import json
from io import StringIO


# instantiate client
s3 = boto3.client('s3')
sns = boto3.client('sns')

# global variables
S3_BUCKET = os.environ['s3_bucket']
TOPIC_ARN = os.environ['sns_topic']


def lambda_handler(event, context):
    print(event['Records'][0])
    event_name = event['Records'][0]['eventName']
    # bucket = event['Records'][0]['s3']['bucket']['name']
    bucket = S3_BUCKET
    key = event['Records'][0]['s3']['object']['key']
    delete = False

    if event_name == "ObjectRemoved:Delete":
        delete = True
        return send_notification(delete, key, bucket)

    response = s3.get_object(Bucket=bucket, Key=key)
    if response:
        data = response['Body'].read().decode('utf-8')
        email = process_data(data)
        if email:
            sns_response = send_notification(delete, key, bucket, email)
            if sns_response:
                print("SNS publish - successful")
            else:
                print("SNS publish - failed")
        else:
            print("No email found in the CSV")
    else:
        print("Get Object - Failed")
    # return {
    #         'statusCode': 200,
    #         'body': json.dumps('Hello from Lambda! Real Test')
    # }


def process_data(data):
    file = StringIO(data)
    reader = csv.reader(file, delimiter=',')
    emails = {}
    for item in reader:
        if item:
            emails[f"{item[1]} {item[2]}"] = item[3]
    # print(emails)
    return emails


def send_notification(delete, key, bucket, emails=[]):
    if delete:
        subject = "S3 - OBJECT DELETED"
        sns_message = f"{key} is being deleted from the {bucket} bucket"
    else:
        subject = "Object uploaded onto the S3 bucket"
        sns_message = json.dumps(emails, indent=2)

    sns_response = sns.publish(
        TargetArn=TOPIC_ARN,
        Message=sns_message,
        Subject=subject
    )
    return sns_response
