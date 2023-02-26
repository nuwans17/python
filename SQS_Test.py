import json
import boto3

from datetime import datetime
current_time = datetime.now()
formatted_time = current_time.strftime("%H:%M:%S %p")
sqs = boto3.client("sqs")

response = sqs.send_message(
    QueueUrl="https://sqs.us-east-1.amazonaws.com/905169972855/WK15SQS",
    MessageBody=formatted_time
)
print(response)
