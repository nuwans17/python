import boto3
client = boto3.resource('sqs')
response = client.create_queue(QueueName="WK15SQS")

print("Available Queues : URLs")
print(response.url)





#for queue in client.queues.all():
#    print(queue.url)