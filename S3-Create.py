import boto3

aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("week14bucket")

response = bucket.create(
    ACL='public-read',
   )

print(response)
