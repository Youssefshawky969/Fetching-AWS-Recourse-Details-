import boto3
import json

# Initialize the session and clients
session = boto3.Session(region_name="us-east-1")
ec2_client = session.client("ec2")

# Fetch VPC details
vpc_response = ec2_client.describe_vpcs()
vpcs = vpc_response.get("Vpcs", [])

# Fetch EC2 details
ec2_response = ec2_client.describe_instances()
instances = []

for reservation in ec2_response["Reservations"]:
    for instance in reservation["Instances"]:
        instances.append(instance)

# Create a dictionary to store results
data = {
    "VPCs": vpcs,
    "EC2_Instances": instances
}

# Save data as JSON
with open("aws_details.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

print("AWS details have been saved to aws_details.json")
