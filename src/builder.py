import os
import logging
import re
from troposphere import Template, Output, Ref, Export, Sub, GetAtt, Tags, Join, NoValue, Select, GetAZs, Cidr
from troposphere.ec2 import VPCGatewayAttachment, InternetGateway, VPC, VPCCidrBlock, DHCPOptions, VPCDHCPOptionsAssociation, VPCEndpoint, VPCGatewayAttachment, FlowLog, EgressOnlyInternetGateway, SecurityGroup, SecurityGroupRule, EIP, NatGateway, Route, NetworkAcl, NetworkAclEntry, PortRange, Subnet, SubnetRoutetableAssociation, SubnetNetworkAclAssociation, RouteTable, TransitGatewayAttachment
from troposphere.iam import Role
from troposphere.s3 import Bucket, BucketEncryption, BucketPolicy
from troposphere.kms import Key
from troposphere.validators import vpc_endpoint_type
from typing import Union

class builder():
    def __init__(self, name, properties, parameters):
        self.name = self.cloudformation_safe_string(name)
        self.template = Template()
        self.template.set_version('2010-09-09')
        self.resources = {}
        self.outputs = {}
        self.properties = properties
        self.parameters = parameters
        logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        self.logger = logging.getLogger('Builder.builder')
        self.logger.setLevel(int(os.environ.get('Logging', logging.DEBUG)))
        self.required_fields = {
        }
        self.ipv4_regex = re.compile('^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$')
        self.ipv6_regex = re.compile('^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))?$')


    def validate_IPv6_key(self, cidr: str):
        if self.build_allipv6_regex.match(cidr):
            return "Ipv6CidrBlock"
        elif self.ipv4_regex.match(cidr):
            return "CidrBlock"
        else:
            logger.debug("Invalid CIDR: {}".format(cidr))
            return "INVALID_CIDR"

    def cloudformation_safe_string(self: builder, unsafe_string: str) -> str:
        if isinstance(unsafe_string, str):
            unsafe_char = '!@#$%^&*()_'
            safe_string_list = [x for x in unsafe_string if x not in unsafe_char]

            return str(''.join(safe_string_list))
        else:
            raise TypeError('CFN Object Name is not a String')

    def str_2_bool(self, v: bool) -> bool:
        if isinstance(v, bool):
            return v
        else:
            if v.lower() in ('yes', 'true', 't', '1'):
                return True
            else:
                return False

    def has_intrinsic_function(self, value):
        intrinsic_list = ['Fn::Sub', 'Fn::Ref', 'Fn::Base64', 'Fn::Cidr', 'Fn::GetAtt', 'Fn::GetAZs', 'Fn::ImportValue', 'Fn::Join', 'Fn::Select', 'Fn::Split', 'Fn::Transform', 'Ref']
        if type(value) == dict:
            self.logger.debug('Value is of type Dict: {}'.format(value))
            self.logger.debug('Intrinsic List: {}'.format(intrinsic_list))
            self.logger.debug('Value Keys: {}'.format(value.keys()))

            return any(x in intrinsic_list for x in value.keys())

    def resolve_parameters(self, value, parameters):
        self.logger.debug('Parameters: {}'.format(parameters))
        if type(value) == dict:
            pattern = r'\${([\w]*)}'
            resolved = value
            for k, v in resolved.items():
                self.logger.debug('{} {}'.format(k, v))
                results = re.findall(pattern, v)
                self.logger.debug(f'Results: ')
                for item in results:
                    self.logger.debug(f'Found Item {item} in Value')
                    if item in parameters.keys():
                        parameter_value = parameters.get(item, None)
                        self.logger.debug(f'Parameter Value: {parameter_value}')
                        if parameter_value:
                            resolved[k] = re.sub(r'(\${{{}}})'.format(str(item)), str(parameter_value), resolved[k])
                            self.logger.debug(f'Resolved Value: {resolved[k]}')
                return resolved[k]
        elif type(value) == str:
            if value in parameters.keys():
                self.logger.debug('Found Value {} in Parameters'.format(value))
                parameter_value = parameters.get(value, None)
                return parameter_value

    def resolve_intrinsic_function(self, value, parameters):
        return self.resolve_parameters(value, parameters) if self.has_intrinsic_function(value) else value

    def handle_intrinsic_function(self, value):
        return value if self.has_intrinsic_function(value) else value

    def build_troposphere_tags(self, name, tags):
        tags["Name"] = name

        return tags

    def build_all(self):
        self.logger.debug('Calling Build All Function')
        self.logger.debug('Calling Build VPC Baseline')
        self.build_baseline()

    def build_baseline(self):
        self.template.add_resource(
            VPC(
                f"{self.name}VPC",
                CidrBlock=self.properties.get('CIDR'),
                EnableDnsSupport=True,
                EnableDnsHostnames=True,
                InstanceTenancy="default",
                Tags=Tags(self.build_troposphere_tags(self.name, self.properties.get("Tags", {})))
            )
        )

        self.template.add_output(
            Output(
                f"{self.name}VPC",
                Value=Ref(f"{self.name}VPC"),
                Export=Export(
                    Sub(f"${{AWS::StackName}}-VPCid")
                )
            )
        )

        self.template.add_resource(
            DHCPOptions(
                f"{self.properties.get('DHCP', {}).get('Name', 'DHCPOptions')}",
                DomainName=self.properties.get('DHCP', {}).get('Name', 'DHCPOptions'),
                DomainNameServers=self.properties.get('DHCP', {}).get('DNSServers', NoValue),
                NetbiosNameServers=self.properties.get('DHCP', {}).get('NTBServers', NoValue),
                NetbiosNodeType=self.properties.get('DHCP', {}).get('NTBType', NoValue),
                NtpServers=self.properties.get('DHCP', {}).get('NTPServers', NoValue),
                Tags=Tags(self.build_troposphere_tags(self.properties.get('DHCP', {}).get('Name', 'DHCPOptions'), self.properties.get("Tags", {})))
            )
        )

        self.template.add_resource(
            InternetGateway(
                "InternetGateway",
                Tags=Tags(Name="InternetGateway")
            )
        )

        self.template.add_resource(
            VPCGatewayAttachment(
                InternetGatewayId=Ref(InternetGateway),
                VpcId=Ref(f"{self.name}VPC")
            )
        )

        self.template.add_resource()

        if self.properties.get("Details", {}).get("IPv6", None):
            self.template.add_resource(
                VPCCidrBlock(
                    "IPv6Block",
                    AmazonProvidedIpv6CidrBlock=True,
                    VpcId=Ref(f"{self.name}VPC")
                )
            )

            self.template.add_resource(
                EgressOnlyInternetGateway(
                    VpcId=Ref(f"{self.name}VPC")
                )
            )

    def build_vpc_endpoints(self):
        for endpoint, details in self.properties.get("Endpoints", {}).items():
            self.template.add_resource(
                VPCEndpoint(
                    f"{endpoint.replace(',','').replace('.','')}",
                    ServiceName=Join("", ["com.amazonaws.", {"Ref": "AWS::Region"}, ".", endpoint]),
                    VpcEndpointType=vpc_endpoint_type(details.get('Type')),
                    VpcId=Ref(f"{self.name}VPC"),
                    PolicyDocument=details.get('PolicyDocument', NoValue),
                    RouteTableIds=details.get('RouteTableIds') if details.get('Type') == "Gateway" else NoValue,
                    SecurityGroupIds=details.get('SecurityGroupIds') if details.get('Type') == "Interface" else NoValue,
                    SubnetIds=details.get('SubnetIds')
                )
            )

    def build_securitygroup(self):
        for secgroup, details in self.properties.get("SecurityGroups", {}).items():
            self.template.add_resource(
                SecurityGroup(
                    f"{secgroup}",
                    GroupName=secgroup,
                    GroupDescription=details.get("GroupDescription", f"{secgroup} Security Group"),
                    VpcId=Ref(f"{self.name}VPC"),
                    Tags=Tags(details.get("Tags")),
                    SecurityGroupEgress=build_security_group_rules(details.get('SecurityGroupEgress', []))
                )
            )
             
    def build_security_group_rules(self, group_rules: list):
        rules_list: list = []
        for rule in group_rules:
            rules_list.append(
                SecurityGroupRule(
                    IpProtocol=rule[0],
                    FromPort=rule[1],
                    ToPort=rule[2],
                    CidrIp=rule[3],
                    Description=rule[4]
                )
            )
        
        return rules_list
    
    def build_nat_gateway(self):
        for natgw, details in self.properties.get("NATGateways", {}).items():
            self.template.add_resource(
                EIP(
                    f"EIP{natgw}",
                    Domain="VPC"
                )
            )

            self.template.add_resource(
                NatGateway(
                    f"{natgw}",
                    AllocationId=GetAtt(f"EIP{natgw}", "AllocationId"),
                    SubnetId=Ref(details.get("Subnet")),
                    Tags=Tags(details.get("Tags"))
                )
            )

            self.template.add_output(
                f"{natgw}",
                Description=f"{natgw}",
                Value=Ref(f"{natgw}"),
                Export=Export(
                    Sub(f"${{AWS::StackName}}-NATGW-{natgw}")
                )
            )

            for routetable in details.get("RouteTable", []):
                self.template.add_resource(
                    Route(
                        f"{routetable}{natgw}",
                        DestinationCidrBlock="0.0.0.0/0",
                        NatGatewayId=Ref(natgw),
                        RouteTableId=Ref(routetable)
                    )
                )

                if self.properties.get("Details", {}).get("IPv6", None):
                    self.template.add_resource(
                        Route(
                            f"{routetable}{natgw}IPv6",
                            DestinationCidrBlock="::/0",
                            EgressOnlyInternetGatewayId=Ref("EgressGateway"),
                            RouteTableId=Ref(routetable)
                        )
                    )
    
    def build_network_acls(self):
        for networkacl, details in self.properties.get("NetworkACLs", {}).items:
            self.template.add_resource(
                NetworkAcl(
                    f"{networkacl}",
                    VpcId=Ref(f"{self.name}VPC"),
                    Tags=Tags(details.get("Tags"))
                )
            )

            for acl_name, acl_detail in networkacl.items():
                acl_detail_list = acl_detail.split(',')
                self.template.add_resource(
                    NetworkAclEntry(
                        f"{acl_name}",
                        CidrBlock=acl_detail_list[4],
                        Egress=acl_detail_list[3],
                        NetworkAclId=Ref(networkacl),
                        PortRange=PortRange(
                            From=acl_detail_list[5],
                            To=acl_detail_list[6]
                        ),
                        Protocol=acl_detail_list[1],
                        RuleAction=acl_detail_list[2],
                        RuleNumber=acl_detail_list[0]
                    )
                )

            self.template.add_output(
                f"{networkacl}",
                Description=f"{networkacl}",
                Value=Ref(f"{networkacl}"),
                Export=Export(
                    Sub(f"${{AWS::StackName}}-NACL-{networkacl}")
                )
            )
    
    def build_subnets(self):
        subnet_count: int = 0
        for subnet, details in self.properties.get("Subnet", {}).items:

            self.template.add_resource(
                Subnet(
                    f"{subnet}",
                    AssignIpv6AddressOnCreation=True if "IPv6" in self.properties("Details", {}) else False,
                    AvailabilityZone=Select(details.get("AZ", 0), GetAZs()),
                    CidrBlock=details.get("CIDR"),
                    Ipv6CidrBlock=Select(details.get("IPv6Iter"), Cidr(Select(0, GetAtt(f"{self.name}VPC", "Ipv6CidrBlocks")) ,subnet_count, 64)) if "IPv6" in self.properties("Details", {}) else NoValue,
                    VpcId=Ref(f"{self.name}VPC"),
                    Tags=Tags(details.get("Tags"))
                )
            )

            self.template.add_resource(
                SubnetRoutetableAssociation(
                    f"{subnet}SubnetRoutetableAssociation",
                    RouteTableId=details.get("RouteTable"),
                    SubnetId=subnet
                )
            )

            self.template.add_resource(
                SubnetNetworkAclAssociation(
                    f"{subnet}SubnetNetworkACLAssociation",
                    NetworkAclId=details.get("NetACL"),
                    SubnetId=subnet
                )
            )

            self.template.add_output(
                f"{subnet}",
                Description=f"{subnet}",
                Value=Ref(f"{subnet}"),
                Export=Export(
                    Sub(f"${{AWS::StackName}}-Subnet-{subnet}")
                )
            )
    
    def build_route_tables(self):
        for routetable, details in self.properties.get("RouteTables").items:
            self.template.add_resource(
                RouteTable(
                    f"{routetable}",
                    VpcId=Ref(f"{self.name}VPC"),
                    Tags=Tags(details.get("Tags"))
                )
            )

            self.template.add_output(
                f"{routetable}",
                Description=f"{routetable}",
                Value=Ref(f"{routetable}"),
                Export=Export(
                    Sub(f"${{AWS::StackName}}-RouteTable-{routetable}")
                )
            )

    def build_transit_gateways(self):
        for tgw, details in self.properties.get("TransitGateway").items:
            self.template.add_resource(
                TransitGatewayAttachment(
                    f"{tgw}TransitGWAttach",
                    TransitGatewayId=details.get("TransitGatewayId"),
                    SubnetIds=[Ref(x) for x in details.get("Subnets")],
                    VpcId=Ref(f"{self.name}VPC"),
                    Tags=Tags(details.get("Tags"))
                )
            )

            for routetable, routes in details.get('RouteTables', {}):
                for route_dict in routes.items:
                    self.template.add_resource(
                        Route(
                            f"{tgw}{routetable}{details.get('RouteName')}",
                            RouteTableId=Ref(routetable),
                            DestinationCidrBlock=route_dict.get('RouteCIDR'),
                            TransitGatewayId=Ref(tgw),
                            DependsOn=f"{tgw}TransitGWAttach"
                        )
                    )
