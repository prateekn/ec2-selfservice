import boto3
from config import *

count = 0

def get_status(key,secret,location):
    try:
        client = boto3.client('ec2',location,
            aws_access_key_id = key,
            aws_secret_access_key = secret,
        )
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False
    response = client.describe_instances()
    ec2_arr = []
    if len(response['Reservations']) != 0:
        for item in response['Reservations']:
            ec2_dic = {
            "ec2_name" : item['Instances'][0]['InstanceId'],
            "status" : item['Instances'][0]['State']['Name'],
              }
            ec2_arr.append(ec2_dic)
            if item['Instances'][0]['State']['Name'] == 'running':
                global count
                count = count + 1
    return ec2_arr

### launch instance
def start_instance(key,secret,location,image_id,instance_type):
    try:
        client = boto3.client('ec2',location,
            aws_access_key_id = key,
            aws_secret_access_key = secret,
        )
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False
    if count <= fixed_count:
        res = client.run_instances(ImageId=image_id,InstanceType=instance_type,MinCount=1,MaxCount=1)   ## <--- AMI ID
        for instance in res['Instances']:
            instance_name = instance['InstanceId']    ## <--- wat all params u need
        return instance_name
    else:
        return "You Have exceeded the Maximum Number of Instance that can be spawned"


def delete_instance(key,secret,location,del_instance):
    try:
        client = boto3.client('ec2',location,
            aws_access_key_id = key,
            aws_secret_access_key = secret,
        )
    except ClientError as err:
        print("Failed to create boto3 client.\n" + str(err))
        return False
        
    res = client.terminate_instances(InstanceIds = del_instance, DryRun = False)
