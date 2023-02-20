import boto3

ec2 = boto3.resource("ec2")

# find the instances that are running and have tag of Dev
ec2_tag={"Name": "tag:Name" , "Values":['Dev']}

#stop the instances based on the filter

for instance in ec2.instances.filter(Filters=[ec2_tag]):
       
       instance.stop()
       print(f'{instance} stopped')