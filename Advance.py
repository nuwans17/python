import boto3

ec2 = boto3.resource("ec2")


#stop the instances based on the filter

for instance in ec2.instances.filter(Filters=[
                {"Name": "tag:Name", "Values": ["Dev"]},
                {"Name": "instance-state-name", "Values": ["running"]}]):
                    
       instance.stop()
       print(f'{instance} stopped')
       
       
       
       