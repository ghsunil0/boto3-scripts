import json
import boto3
import sys

def lambda_handler(event, context):
    primary_id   = "i-02ba87a4c0196755a"
    secondary_id = "i-01df563afab6f9cb2"
    secondary_ip = "172.31.22.155"

    ec2_re=boto3.resource("ec2","us-east-2")
    ec2_cli=boto3.client("ec2","us-east-2") 

    primary_instance  = ec2_re.Instance(primary_id)
    secondary_instance= ec2_re.Instance(secondary_id)

    if primary_instance.state['Name'] == "running":
        print("Master is running. so no modifications")
    else:
        pnetwork_interface_Info=primary_instance.network_interfaces_attribute[0]
        snetwork_interface_Info=secondary_instance.network_interfaces_attribute[0]
        pnw_interface_id=pnetwork_interface_Info['NetworkInterfaceId']
        snw_interface_id=snetwork_interface_Info['NetworkInterfaceId']

        ec2_cli.unassign_private_ip_addresses(
                NetworkInterfaceId=pnw_interface_id,
                PrivateIpAddresses=[secondary_ip]
                )
    
        ec2_cli.assign_private_ip_addresses(
            AllowReassignment=True,
            NetworkInterfaceId=snw_interface_id,
            PrivateIpAddresses=[secondary_ip]
            )
    return None
