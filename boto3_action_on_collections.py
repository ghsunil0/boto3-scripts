import boto3
from pprint import pprint 

# This is an example of collection of services or group of resources
# In resources ec2 - service resources
# we have 3 sets of available services
# 1 create/modify resource
# 2 group of resources and
# 3 collection of resources 
#   3 eg : for ec2 - Images, instances, internet_gw, key-pairs, route-tables
#                    security-groups  , snap-shots , volumes  , vpcs etc
#   resource.instances (all, limit, filter)
#      Also : For filter the format should be
#         instance_iterator = ec2.instances.filter(
#           Filters=[
#                    {
#                      'Name': 'string',
#                      'Values': [
#                                'string',
#                                ]
#                   },
#
#               name=instance-state-name
#               value = (pending | running | shutting-down | terminated | stopping | stopped ).
#          filter condition should be filt_f1{"Name":"", "Value":[""]}
#
#  ========================================
#  The second part for collection objects
#    is actions that can be taken on collection of objects
#
#  actions like Create_tags, monitor, unmonitor,
#               start,  stop,  reboot, terminate
#
#

# define session connection management console
man_con_ec2_dev=boto3.session.Session(profile_name='ec2-developer')

# ec2 console using resource and client sessions

ec2_con_res=man_con_ec2_dev.resource(service_name='ec2',region_name='us-east-2')
ec2_con_cli=man_con_ec2_dev.client  (service_name='ec2',region_name='us-east-2')

# Collecting all instance ids
all_instances_ids=[]
for each_inst in ec2_con_res.instances.all():
    all_instances_ids.append(each_inst.id)
print (all_instances_ids)

# Collection of all dev instances
dev_instances_ids=[]
filt_1 = {"Name": "tag:Name", "Values":['dev']}
for each_inst in ec2_con_res.instances.filter(Filters=[filt_1]):
    print ("tag = dev for instance : ", each_inst.id)
    dev_instances_ids.append(each_inst.id)

# print ("instance ids with tag - 'dev'")
# print (dev_instances_ids)

print ("Starting instances with ids of : ", dev_instances_ids)
ec2_con_cli.start_instances(InstanceIds=dev_instances_ids)
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=dev_instances_ids)
print ("Your dev instances are up and running ")


# The below code is the previous exercise
#   to start all instances with no condition


waiter=ec2_con_cli.get_waiter('instance_running')
print("Starting all instances ......")
ec2_con_res.instances.start()
waiter.wait(InstanceIds=all_instances_ids)
print("All Instances are up and running")

# print options available for collection of resources ec2-instances
# pprint (ec2_con_res.instances.all())

filt_1={"Name": "instance-state-name", "Values":['running']}
# print (filt_1)
filt_2={"Name": "instance-state-name", "Values":['running' ,'stopped']}
filt_3={"Name": "instance-type"      , "Values":['t2.micro']}
print (filt_2)
print (filt_3)
#for each_obj in (ec2_con_res.instances.all()):
#for each_obj in (ec2_con_res.instances.limit(1)):
#for each_obj in (ec2_con_res.instances.filter(Filters=[filt_1])):
#for each_obj in (ec2_con_res.instances.filter(Filters=[filt_2])):
for each_obj in (ec2_con_res.instances.filter(Filters=[filt_2, filt_3])):
    print ('Instance id is : {} '.format(each_obj.id))
           

 
