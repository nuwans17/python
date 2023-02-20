import boto3

ec2 = boto3.resource("ec2")


#stop the instances based on the filter
def stop_ec2_dev(ec2):

for instance in ec2.instances.filter(Filters=[
                {"Name": "tag:Name", "Values": ["Dev"]},
                {"Name": "instance-state-name", "Values": ["running"]}]):
       Instance_id=instance.id
	   if("i-067244dc962ac72c9" != id):
	              ec2.instances.filter(InstanceIds=[Instance_id]).stop()
	      
#       instance.stop()
       print(f'{instance} stopped')