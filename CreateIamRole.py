import boto3
import json

client = boto3.client('iam')
assume_role_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]   
}
response = client.create_role(
    RoleName='SQS_Role_Wk15',
    AssumeRolePolicyDocument=json.dumps(assume_role_policy),
    Description='Create a new iam role for SQS',
    MaxSessionDuration=3600,
    )

print(response)