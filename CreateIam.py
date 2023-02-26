import json

import boto3

# Create IAM client
iam = boto3.client('iam')

# Create a policy
my_managed_policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:sqs:us-east-1:905169972855:WK15SQS"
        },
        {
            "Effect": "Allow",
            "Action": [
                "sqs:ReceiveMessage",
                "sqs:SendMessage",
                "sqs:GetQueueAttributes"
            ],
            "Resource": "arn:aws:sqs:us-east-1:905169972855:WK15SQS"
        }
    ]
}
response = iam.create_policy(
  PolicyName='mysqsPolicy',
  PolicyDocument=json.dumps(my_managed_policy)
)
print(response)

