import boto3

#
# Script to demonstrate meta objects
#
#    Some times you may want to access client objects from the
#    resource (not client session)
#    eg : client.describe_region() to get the region ids
#    in that case you can use resource meta objects resource.meta
#    in resource.meta you have client object as resource.meta.client
#    and that's way to get to client objects
#    resource.meta.client.describe_region()['Region'] - collection
#    for each resource.meta.client.describe_region()['Region'] for each region
#
#



# define management console sessions for admin and ec2-developer

man_con_admin   =boto3.session.Session(profile_name='sunil-admin')
man_con_ec2_dev =boto3.session.Session(profile_name='ec2-developer')

# define ec2 console for resource and client

ec2_dev_con_res = man_con_ec2_dev.resource(service_name='ec2')
ec2_dev_con_cli = man_con_ec2_dev.client  (service_name='ec2')

# the below will display all available options
# print (dir(ec2_dev_con_res))
"""
['ClassicAddress', 'DhcpOptions', 'Image', 'Instance', 'InternetGateway', 'KeyPair',
'NetworkAcl', 'NetworkInterface', 'NetworkInterfaceAssociation', 'PlacementGroup',
'Route', 'RouteTable', 'RouteTableAssociation', 'SecurityGroup', 'Snapshot',
'Subnet', 'Tag', 'Volume', 'Vpc', 'VpcAddress', 'VpcPeeringConnection',
'__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
'__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
'__str__', '__subclasshook__', '__weakref__',
'classic_addresses',
'create_dhcp_options', 'create_instances', 'create_internet_gateway',
'create_key_pair', 'create_network_acl', 'create_network_interface',
'create_placement_group', 'create_route_table', 'create_security_group',
'create_snapshot', 'create_subnet', 'create_tags', 'create_volume',
'create_vpc', 'create_vpc_peering_connection', 'dhcp_options_sets',
'disassociate_route_table', 'get_available_subresources', 'images',
'import_key_pair', 'instances', 'internet_gateways', 'key_pairs',
'meta',
'network_acls', 'network_interfaces', 'placement_groups',
'register_image', 'route_tables', 'security_groups', 'snapshots',
'subnets', 'volumes', 'vpc_addresses', 'vpc_peering_connections', 'vpcs']
"""


# the below will display all available options for meta 
# print (dir(ec2_dev_con_res.meta))
"""
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
 '__str__', '__subclasshook__', '__weakref__',
 'client',
 'copy', 'data', 'identifiers', 'resource_model', 'service_name']
"""

for each_obj in (ec2_dev_con_res.meta.client.describe_regions()['Regions']):
    print ("Region Name : {} ".format(each_obj['RegionName']))
























