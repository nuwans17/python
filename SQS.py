import json
import boto3
from datetime import datetime

QUEUE_URL="https://sqs.us-east-1.amazonaws.com/905169972855/WK15SQS"

def sqs_client():
    sqs = boto3.client('sqs', region_name='us-east-1')
    """ :type : pyboto3.sqs """
    return sqs
    
def send_message_to_queue():
    current_time = datetime.now()
    
    return sqs_client().send_message(
        QueueUrl='QUEUE_URL',
        MessageBody=(current_time)
    )

