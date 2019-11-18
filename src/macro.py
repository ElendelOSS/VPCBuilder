import json
import traceback
import os
import re
import logging

logging.basicConfig(format='%(asctime)s [%(levelname)s] (%(funcName)s) %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
logger = logging.getLogger("VPCBuilder.Macro")
logger.setLevel(int(os.environ.get("Logging", logging.INFO)))

ipv4_regex = re.compile('^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$')
ipv6_regex = re.compile('^s*((([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:))|(([0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3})|:))|(([0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(([0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:))|(:(((:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]d|1dd|[1-9]?d)(.(25[0-5]|2[0-4]d|1dd|[1-9]?d)){3}))|:)))(%.+)?s*(\/([0-9]|[1-9][0-9]|1[0-1][0-9]|12[0-8]))?$')


def isIPv6NetACL(cidr):
    if ipv6_regex.match(cidr):
        return "Ipv6CidrBlock"
    elif ipv4_regex.match(cidr):
        return "CidrBlock"
    else:
        logger.debug("Invalid CIDR: {}".format(cidr))
        return "INVALID_CIDR"


def isIPv6Route(cidr):
    if ipv6_regex.match(cidr):
        return "DestinationIpv6CidrBlock"
    elif ipv4_regex.match(cidr):
        return "DestinationCidrBlock"
    else:
        logger.debug("Invalid CIDR: {}".format(cidr))
        return "INVALID_CIDR"


def str2bool(v):
    if v.lower() in ("yes", "true", "t", "1"):
        return True
    else:
        return False


def hasIntrinsicFunction(value):
    intrinsic_list = ["Fn::Sub", "Fn::Ref", "Fn::Base64", "Fn::Cidr", "Fn::GetAtt", "Fn::GetAZs", "Fn::ImportValue", "Fn::Join", "Fn::Select", "Fn::Split", "Fn::Transform", "Ref"]
    if type(value) == dict:
        logger.debug("Value is of type Dict: {}".format(value))
        logger.debug("Intrinsic List: {}".format(intrinsic_list))
        logger.debug("Value Keys: {}".format(value.keys()))

        return any(x in intrinsic_list for x in value.keys())


def resolveParameters(value, parameter):
    logger.debug("Parameters: {}".format(parameter))
    if type(value) == dict:
        pattern = "\${([\w]*)}"
        resolved = value
        for k, v in resolved.items():
            logger.debug("{} {}".format(k, v))
            results = re.findall(pattern, v)
            for item in results:
                logger.debug("Found Item {} in Value".format(item))
                if item in parameter.keys():
                    parameter_value = parameter.get(item, None)
                    if parameter_value:
                        resolved[k] = re.sub("(\${{{}}})".format(str(item)), str(parameter_value), resolved[k])
            return resolved[k]
    elif type(value) == str:
        if value in parameter.keys():
            logger.debug("Found Value {} in Parameters".format(value))
            parameter_value = parameter.get(value, None)
            return parameter_value


def resolveIntrinsicFunction(value, parameters):
    return resolveParameters(value, parameters) if hasIntrinsicFunction(value) else value


def handleIntrinsicFunction(value):
    return value if hasIntrinsicFunction(value) else {"Ref": value}


def resolveCIDRParameter(value, parameters):
    return value if ipv4_regex.match(value) or ipv6_regex.match(value) else resolveParameters(value, parameters)


def handleCIDRParameter(value):
    return value if ipv4_regex.match(value) or ipv6_regex.match(value) else {"Ref": value}


def buildTags(tags):
    generated_tags = []
    for k, v in tags.items():
        generated_tags.append(
            {
                "Key": k,
                "Value": v
            }
        )

    return generated_tags


def buildTransitGateways(properties, resources, outputs, parameters):
    for transitgw, objects in properties["TransitGateways"].items():
        resources["{}TransitGWAttach".format(transitgw)] = {
            "Type": "AWS::EC2::TransitGatewayAttachment",
            "Properties": {
                "TransitGatewayId": objects["TransitGatewayId"],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }

        resources["{}TransitGWAttach".format(transitgw)]["Properties"]["SubnetIds"] = []
        for subnet in objects["Subnets"]:
            resources[transitgw + "TransitGWAttach"]["Properties"]["SubnetIds"].append(
                {
                    "Ref": subnet
                }
            )
        resources["{}TransitGWAttach".format(transitgw)]["Properties"]["Tags"] = []
        for k, v in objects["Tags"].items():
            resources[transitgw + "TransitGWAttach"]["Properties"]["Tags"].append(
                {
                    "Key": k,
                    "Value": v
                }
            )

        if properties["Tags"]:
            resources["{}TransitGWAttach".format(transitgw)]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

        if "RouteTables" in objects:
            for routetable, routes in objects["RouteTables"].items():
                for route in routes:
                    resources["{}{}{}".format(transitgw, routetable, route["RouteName"])] = {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            isIPv6Route(route["RouteCIDR"]): route["RouteCIDR"],
                            "TransitGatewayId": objects["TransitGatewayId"],
                            "RouteTableId": {
                                "Ref": routetable
                            }
                        },
                        "DependsOn": [
                            "{}TransitGWAttach".format(transitgw)
                        ]
                    }

    return resources, outputs


def buildRouteTables(properties, resources, outputs, parameters):
    for routetable, objects in properties["RouteTables"].items():
        resources[routetable] = {
            "Type": "AWS::EC2::RouteTable",
            "Properties": {
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": routetable
                    }
                ],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }

        if properties["Tags"]:
            resources[routetable]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

        outputs[routetable] = {
            "Description": routetable,
            "Value": {
                "Ref": routetable
            },
            "Export": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-RouteTable-" + routetable
                }
            }
        }

        if "VGW" in parameters:
            resources[routetable + "RoutePropagation"] = {
                "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                "Properties": {
                    "RouteTableIds": [
                        {
                            "Ref": routetable
                        }
                    ],
                    "VpnGatewayId": {
                        "Ref": "VGW"
                    }
                },
                "DependsOn": [
                    "VPCGatewayAttachment"
                ]
            }

        if objects is not None:
            for route in objects:
                resources[route["RouteName"]] = {
                    "Type": "AWS::EC2::Route",
                    "Properties": {
                        isIPv6Route(route["RouteCIDR"]): route["RouteCIDR"],
                        "GatewayId": {
                            "Ref": route["RouteGW"]
                        },
                        "RouteTableId": {
                            "Ref": routetable
                        }
                    }
                }

    return resources, outputs


def buildSubnets(properties, resources, outputs, parameters):
    subnet_count = 0
    for subnet, objects in properties["Subnets"].items():
        resources[subnet] = {
            "Type": "AWS::EC2::Subnet",
            "Properties": {
                "AvailabilityZone": {
                    "Fn::Select": [
                        objects["AZ"],
                        {
                            "Fn::GetAZs": ""
                        }
                    ]
                },
                "CidrBlock": objects["CIDR"],
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": subnet
                    }
                ],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }
        if properties["Tags"]:
            resources[subnet]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

        outputs[subnet] = {
            "Description": subnet,
            "Value": {
                "Ref": subnet
            },
            "Export": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-Subnet-" + subnet
                }
            }
        }

        resources[subnet + "SubnetRoutetableAssociation"] = {
            "Type": "AWS::EC2::SubnetRouteTableAssociation",
            "Properties": {
                "RouteTableId": {
                    "Ref": objects["RouteTable"]
                },
                "SubnetId": {
                    "Ref": subnet
                }
            }
        }

        resources[subnet + "SubnetNetworkACLAssociation"] = {
            "Type": "AWS::EC2::SubnetNetworkAclAssociation",
            "Properties": {
                "NetworkAclId": {
                    "Ref": objects["NetACL"]
                },
                "SubnetId": {
                    "Ref": subnet
                }
            }
        }
        subnet_count = subnet_count + 1

    if "IPv6" in properties["Details"]:
        subnet_itr = 0
        for subnet, objects in properties["Subnets"].items():
            if properties["Details"]["IPv6"]:
                resources[subnet]["DependsOn"] = "IPv6Block"
                resources[subnet]["Properties"]["AssignIpv6AddressOnCreation"] = True
                resources[subnet]["Properties"]["Ipv6CidrBlock"] = {
                    "Fn::Select": [
                        objects["IPv6Iter"],
                        {
                            "Fn::Cidr": [
                                {
                                    "Fn::Select": [
                                        0,
                                        {
                                            "Fn::GetAtt": [
                                                resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters),
                                                "Ipv6CidrBlocks"
                                            ]
                                        }
                                    ]
                                },
                                subnet_count,
                                64
                            ]
                        }
                    ]
                }
                subnet_itr = subnet_itr + 1

    return resources, outputs


def buildNetworlACLs(properties, resources, outputs, parameters):
    for networkacl, objects in properties["NetworkACLs"].items():
        resources[networkacl] = {
            "Type": "AWS::EC2::NetworkAcl",
            "Properties": {
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": networkacl
                    }
                ],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }

        if properties["Tags"]:
            resources[networkacl]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

        outputs[networkacl] = {
            "Description": networkacl,
            "Value": {
                "Ref": networkacl
            },
            "Export": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-NACL-" + networkacl
                }
            }
        }

        for entry, rule in objects.items():
            splitset = rule.split(',')
            resources[entry] = {
                "Type": "AWS::EC2::NetworkAclEntry",
                "Properties": {
                    isIPv6NetACL(resolveCIDRParameter(splitset[4], parameters)): handleCIDRParameter(splitset[4]),
                    "Egress": str2bool(splitset[3]),
                    "NetworkAclId": {
                        "Ref": networkacl
                    },
                    "PortRange": {
                        "From": int(splitset[5]),
                        "To": int(splitset[6])
                    },
                    "Protocol": int(splitset[1]),
                    "RuleAction": splitset[2],
                    "RuleNumber": int(splitset[0])
                }
            }

    return resources, outputs


def buildNATGateways(properties, resources, outputs, parameters):
    for natgw, objects in properties["NATGateways"].items():
        resources["EIP" + natgw] = {
            "Type": "AWS::EC2::EIP",
            "Properties": {
                "Domain": "vpc"
            }
        }

        outputs["EIP" + natgw] = {
            "Description": "EIP for " + natgw,
            "Value": {
                "Ref": "EIP" + natgw
            },
            "Export": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-EIP-" + natgw
                }
            }
        }

        resources[natgw] = {
            "Type": "AWS::EC2::NatGateway",
            "Properties": {
                "AllocationId": {
                    "Fn::GetAtt": [
                        "EIP" + natgw,
                        "AllocationId"
                    ]
                },
                "SubnetId": {
                    "Ref": objects["Subnet"]
                },
                "Tags": [
                    {
                        "Key": "Name",
                        "Value": natgw
                    }
                ]
            }
        }

        if properties["Tags"]:
            resources[natgw]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

        outputs[natgw] = {
            "Description": natgw,
            "Value": {
                "Ref": natgw
            },
            "Export": {
                "Name": {
                    "Fn::Sub": "${AWS::StackName}-NATGW-" + natgw
                }
            }
        }

        if isinstance(objects["Routetable"], list):
            logger.debug("Routetable is of type list no conversion")
            routetable_list = objects["Routetable"]
        else:
            logger.debug("Routetable is of type list no conversion")
            routetable_list = [objects["Routetable"]]

        for routetable in routetable_list:
            resources["{}{}".format(str(routetable), natgw)] = {
                "Type": "AWS::EC2::Route",
                "Properties": {
                    "DestinationCidrBlock": "0.0.0.0/0",
                    "NatGatewayId": {
                        "Ref": natgw
                    },
                    "RouteTableId": {
                        "Ref": routetable
                    }
                }
            }

            if "IPv6" in properties["Details"]:
                if properties["Details"]["IPv6"]:
                    resources["{}{}IPv6".format(str(routetable), natgw)] = {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": routetable
                            }
                        }
                    }

    return resources, outputs


def buildSecurityGroups(properties, resources, outputs, parameters):
    for secgroup, objects in properties["SecurityGroups"].items():
        resources[secgroup] = {
            "Type": "AWS::EC2::SecurityGroup",
            "Properties": {
                "GroupName": secgroup,
                "GroupDescription": objects["GroupDescription"],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }

        if "SecurityGroupIngress" in objects:
            resources[secgroup]["Properties"]["SecurityGroupIngress"] = []
            for rule in objects["SecurityGroupIngress"]:
                resources[secgroup]["Properties"]["SecurityGroupIngress"].append({
                    "IpProtocol": rule[0],
                    "FromPort": rule[1],
                    "ToPort": rule[2],
                    "CidrIp": rule[3],
                    "Description": rule[4]
                })

        if "SecurityGroupEgress" in objects:
            resources[secgroup]["Properties"]["SecurityGroupEgress"] = []
            for rule in objects["SecurityGroupEgress"]:
                resources[secgroup]["Properties"]["SecurityGroupEgress"].append({
                    "IpProtocol": rule[0],
                    "FromPort": rule[1],
                    "ToPort": rule[2],
                    "CidrIp": rule[3],
                    "Description": rule[4]
                })
        if "Tags" in objects:
            resources[secgroup]["Properties"]["Tags"] = []
            for k, v in objects["Tags"].items():
                resources[secgroup]["Properties"]["Tags"].append({
                    "Key": k,
                    "Value": v
                })

        if properties["Tags"]:
            resources[secgroup]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

    return resources, outputs


def buildVPCEndpoints(properties, resources, outputs, parameters):
    for endpoint, objects in properties["Endpoints"].items():
        santisedendpoint = endpoint.replace("-", "").replace(".", "")
        resources[santisedendpoint + "EndPoint"] = {
            "Type": "AWS::EC2::VPCEndpoint",
            "Properties": {
                "ServiceName": {"Fn::Join": ["", ["com.amazonaws.", {"Ref": "AWS::Region"}, "." + endpoint]]},
                "VpcEndpointType": objects["Type"],
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
            }
        }

        if objects["Type"] == "Gateway":
            if "PolicyDocument" in objects:
                resources[santisedendpoint + "EndPoint"]["Properties"]["PolicyDocument"] = objects["PolicyDocument"]
            if "RouteTableIds" in objects:
                resources[santisedendpoint + "EndPoint"]["Properties"]["RouteTableIds"] = []
                for routetable in objects["RouteTableIds"]:
                    resources[santisedendpoint + "EndPoint"]["Properties"]["RouteTableIds"].append({"Ref": routetable})

        if objects["Type"] == "Interface":
            resources[santisedendpoint + "EndPoint"]["Properties"]["PrivateDnsEnabled"] = True
            if "SubnetIds" in objects:
                resources[santisedendpoint + "EndPoint"]["Properties"]["SubnetIds"] = []
                for subnet in objects["SubnetIds"]:
                    resources[santisedendpoint + "EndPoint"]["Properties"]["SubnetIds"].append({"Ref": subnet})
            if "SecurityGroupIds" in objects:
                resources[santisedendpoint + "EndPoint"]["Properties"]["SecurityGroupIds"] = []
                for secgroup in objects["SecurityGroupIds"]:
                    resources[santisedendpoint + "EndPoint"]["Properties"]["SecurityGroupIds"].append({"Ref": secgroup})

    return resources, outputs


def buildBaseline(properties, resources, outputs, parameters):
    logger.debug("VPC Details {}".format(properties.get("Details")))
    resources[resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)] = {
        "Type": "AWS::EC2::VPC",
        "Properties": {
            "CidrBlock": properties["CIDR"],
            "EnableDnsHostnames": True,
            "EnableDnsSupport": True,
            "InstanceTenancy": "default",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)
                }
            ]
        }
    }

    if properties["Tags"]:
        resources[resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

    outputs[resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)] = {
        "Description": resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters),
        "Value": handleIntrinsicFunction(properties["Details"]["VPCName"]),
        "Export": {
            "Name": {
                "Fn::Sub": "${AWS::StackName}-VPCid"
            }
        }
    }

    if "IPv6" in properties["Details"]:
        if properties["Details"]["IPv6"]:
            resources["IPv6Block"] = {
                "Type": "AWS::EC2::VPCCidrBlock",
                "Properties": {
                    "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)),
                    "AmazonProvidedIpv6CidrBlock": True
                }
            }

            resources["EgressGateway"] = {
                "Type": "AWS::EC2::EgressOnlyInternetGateway",
                "Properties": {
                    "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
                }
            }

    resources[properties["DHCP"]["Name"]] = {
        "Type": "AWS::EC2::DHCPOptions",
        "Properties": {
            "DomainNameServers": [properties["DHCP"]["DNSServers"]],
            "NtpServers": [properties["DHCP"]["NTPServers"]],
            "NetbiosNodeType": properties["DHCP"]["NTBType"],
            "Tags": [{
                "Key": "Name",
                "Value": properties["DHCP"]["Name"]
            }]
        }
    }

    if properties["Tags"]:
        resources[properties["DHCP"]["Name"]]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

    resources[properties["DHCP"]["Name"] + "Association"] = {
        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
        "Properties": {
            "DhcpOptionsId": {
                "Ref": properties["DHCP"]["Name"]
            },
            "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
        }
    }

    resources["InternetGateway"] = {
        "Type": "AWS::EC2::InternetGateway",
        "Properties": {
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "InternetGateway"
                }
            ]
        }
    }

    if properties["Tags"]:
        resources["InternetGateway"]["Properties"]["Tags"].extend(buildTags(properties["Tags"]))

    resources["IGWVPCGatewayAttachment"] = {
        "Type": "AWS::EC2::VPCGatewayAttachment",
        "Properties": {
            "InternetGatewayId": {
                "Ref": "InternetGateway"
            },
            "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters))
        }
    }

    if "VGW" in parameters:
        resources["VPCGatewayAttachment"] = {
            "Type": "AWS::EC2::VPCGatewayAttachment",
            "Properties": {
                "VpcId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)),
                "VpnGatewayId": {
                    "Ref": "VGW"
                }
            }
        }

    resources["VPCFlowLogsRole"] = {
        "Type": "AWS::IAM::Role",
        "Properties": {
            "AssumeRolePolicyDocument": {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Effect": "Allow",
                        "Principal": {
                            "Service": [
                                "vpc-flow-logs.amazonaws.com"
                            ]
                        },
                        "Action": [
                            "sts:AssumeRole"
                        ]
                    }
                ]
            },
            "Path": "/",
            "Policies": [
                {
                    "PolicyName": "root",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [
                            {
                                "Effect": "Allow",
                                "Action": [
                                    "logs:*"
                                ],
                                "Resource": "arn:aws:logs:*:*:*"
                            }
                        ]
                    }
                }
            ]
        }
    }

    resources["VPCFlowLogs"] = {
        "Type": "AWS::EC2::FlowLog",
        "Properties": {
            "DeliverLogsPermissionArn": {
                "Fn::GetAtt": ["VPCFlowLogsRole", "Arn"]
            },
            "LogGroupName": "FlowLogsGroup",
            "ResourceId": handleIntrinsicFunction(resolveIntrinsicFunction(properties["Details"]["VPCName"], parameters)),
            "ResourceType": "VPC",
            "TrafficType": "ALL"
        }
    }

    return resources, outputs


def handler(event, context):
    print(json.dumps(event))
    macro_response = {
        "requestId": event["requestId"],
        "status": "success"
    }
    try:
        params = {
            "params": event["templateParameterValues"],
            "template": event["fragment"],
            "account_id": event["accountId"],
            "region": event["region"]
        }
        resources = {}
        outputs = {}
        response = event["fragment"]
        parameters = event.get("templateParameterValues", {})
        for k in list(response["Resources"].keys()):
            if response["Resources"][k]["Type"] == "Versent::Network::VPC":
                if "Properties" in response["Resources"][k]:
                    properties = response["Resources"][k]["Properties"]

                    resources, outputs = buildBaseline(properties, resources, outputs, parameters)

                    if "TransitGateways" in properties:
                        resources, outputs = buildTransitGateways(properties, resources, outputs, parameters)

                    if "RouteTables" in properties:
                        resources, outputs = buildRouteTables(properties, resources, outputs, parameters)

                    if "Subnets" in properties:
                        resources, outputs = buildSubnets(properties, resources, outputs, parameters)

                    if "NetworkACLs" in properties:
                        resources, outputs = buildNetworlACLs(properties, resources, outputs, parameters)

                    if "NATGateways" in properties:
                        resources, outputs = buildNATGateways(properties, resources, outputs, parameters)

                    if "SecurityGroups" in properties:
                        resources, outputs = buildSecurityGroups(properties, resources, outputs, parameters)

                    if "Endpoints" in properties:
                        resources, outputs = buildVPCEndpoints(properties, resources, outputs, parameters)

        response["Resources"] = resources
        response["Outputs"] = outputs
        macro_response["fragment"] = response
    except Exception as e:
        traceback.print_exc()
        macro_response["status"] = "failure"
        macro_response["errorMessage"] = str(e)

    print(json.dumps(macro_response))
    return macro_response
