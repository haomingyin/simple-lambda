import json
import boto3

def handler(event, context):
    print("Hello World")
    print(event)
    with open('./.bumpversion.cfg') as file:
        print(file.read())