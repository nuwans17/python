import boto3
ec2 = boto3.resource('ec2')
tags = [
           {'Key':'Name','Value': 'Dev'},
        ]
               
tag_specification = [{'ResourceType': 'instance', 'Tags': tags},]

instances = ec2.create_instances(
        ImageId="ami-065bb5126e4504910",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="KP14",
        TagSpecifications=tag_specification
 )