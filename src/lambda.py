import json
import traceback

def isIPv6NetACL(cidr):
    if cidr == "::/0":
        return "Ipv6CidrBlock"
    else:
        return "CidrBlock"

def isIPv6Route(cidr):
    if cidr == "::/0":
        return "DestinationIpv6CidrBlock"
    else:
        return "DestinationCidrBlock"

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
        for k in list(response["Resources"].keys()):
            if response["Resources"][k]["Type"] == "Kablamo::Network::VPC":
                if "Properties" in response["Resources"][k]:
                    properties = response["Resources"][k]["Properties"]
                    resources[properties["Details"]["VPCName"]] = {
                        "Type": "AWS::EC2::VPC",
                        "Properties": {
                            "CidrBlock": properties["CIDR"],
                            "EnableDnsHostnames": "true",
                            "EnableDnsSupport": "true",
                            "InstanceTenancy": "default",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": properties["Details"]["VPCName"]
                                }
                            ]
                        }
                    }

                    outputs[properties["Details"]["VPCName"]] = {
                        "Description": properties["Details"]["VPCName"],
                        "Value": { 
                            "Ref" : properties["Details"]["VPCName"] 
                        },
                        "Export" : { 
                            "Name" : {
                                "Fn::Sub": "${AWS::StackName}-VPCid" 
                            }
                        }
                    }

                    if "IPv6" in properties["Details"]:
                        if properties["Details"]["IPv6"]:
                            resources["IPv6Block"] = {
                                "Type": "AWS::EC2::VPCCidrBlock",
                                "Properties": {
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    },
                                    "AmazonProvidedIpv6CidrBlock": "true"
                                }
                            }
                        
                            resources["EgressGateway"] = {
                                "Type": "AWS::EC2::EgressOnlyInternetGateway",
                                "Properties": {
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
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

                    resources[properties["DHCP"]["Name"]+"Association"] = {
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
                        "Properties": {
                            "DhcpOptionsId": {
                                "Ref": properties["DHCP"]["Name"]
                            },
                            "VpcId": {
                                "Ref": properties["Details"]["VPCName"]
                            }
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

                    resources["IGWVPCGatewayAttachment"] = {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "VpcId": {
                                "Ref": properties["Details"]["VPCName"]
                            }
                        }
                    }

                    resources["VPCGatewayAttachment"] = {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "VpcId": {
                                "Ref": properties["Details"]["VPCName"]
                            },
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
                        "Type" : "AWS::EC2::FlowLog",
                        "Properties" : {
                            "DeliverLogsPermissionArn" : { 
                                "Fn::GetAtt" : ["VPCFlowLogsRole", "Arn"] 
                            },
                            "LogGroupName" : "FlowLogsGroup",
                            "ResourceId" : { 
                                "Ref" : properties["Details"]["VPCName"]
                            },
                            "ResourceType" : "VPC",
                            "TrafficType" : "ALL"
                        }
                    }

                    if "TransitGateways" in properties:
                        for transitgw, objects in properties["TransitGateways"].iteritems():
                            resources[transitgw+"TransitGWAttach"] = {
                                "Type": "AWS::EC2::TransitGatewayAttachment",
                                "Properties": {
                                    "TransitGatewayId" : objects["TransitGatewayId"],
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }
                            resources[transitgw+"TransitGWAttach"]["Properties"]["SubnetIds"] = []
                            for subnet in objects["Subnets"]:
                                resources[transitgw+"TransitGWAttach"]["Properties"]["SubnetIds"].append(
                                    { 
                                        "Ref": subnet 
                                    }
                                )
                            resources[transitgw+"TransitGWAttach"]["Properties"]["Tags"] = []
                            for k, v in objects["Tags"].iteritems():
                                resources[transitgw+"TransitGWAttach"]["Properties"]["Tags"].append(
                                    {
                                        "Key" : k,
                                        "Value" : v
                                    }
                                )

                    if "RouteTables" in properties:
                        for routetable, objects in properties["RouteTables"].iteritems():
                            resources[routetable] = {
                                "Type": "AWS::EC2::RouteTable",
                                "Properties": {
                                    "Tags": [
                                        {
                                            "Key": "Name",
                                            "Value": routetable
                                        }
                                    ],
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }

                            outputs[routetable] = {
                                "Description": routetable,
                                "Value": { 
                                    "Ref" : routetable 
                                },
                                "Export" : { 
                                    "Name" : {
                                        "Fn::Sub": "${AWS::StackName}-RouteTable-"+routetable 
                                    }
                                }
                            }

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

                    if "Subnets" in properties:
                        subnet_count = 0
                        for subnet, objects in properties["Subnets"].iteritems():
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
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }

                            outputs[subnet] = {
                                "Description": subnet,
                                "Value": { 
                                    "Ref" : subnet 
                                },
                                "Export" : { 
                                    "Name" : {
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
                            for subnet, objects in properties["Subnets"].iteritems():
                                if properties["Details"]["IPv6"]:
                                    resources[subnet]["DependsOn"] = "IPv6Block"
                                    resources[subnet]["Properties"]["AssignIpv6AddressOnCreation"] = True
                                    resources[subnet]["Properties"]["Ipv6CidrBlock"] = { 
                                        "Fn::Select": [ 
                                            subnet_itr, 
                                            { 
                                                "Fn::Cidr": [
                                                    { 
                                                        "Fn::Select": [
                                                            0, 
                                                            { 
                                                                "Fn::GetAtt": [ 
                                                                    properties["Details"]["VPCName"],
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
                                    subnet_itr = subnet_itr +1
                                    
                    
                    if "NetworkACLs" in properties:
                        for networkacl, objects in properties["NetworkACLs"].iteritems():
                            resources[networkacl] = {
                                "Type": "AWS::EC2::NetworkAcl",
                                "Properties": {
                                    "Tags": [
                                        {
                                            "Key": "Name",
                                            "Value": networkacl
                                        }
                                    ],
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }

                            outputs[networkacl] = {
                                "Description": networkacl,
                                "Value": { 
                                    "Ref" : networkacl 
                                },
                                "Export" : { 
                                    "Name" : {
                                        "Fn::Sub": "${AWS::StackName}-NACL-" + networkacl 
                                    }
                                }
                            }

                            for entry, rule in objects.items():
                                splitset = rule.split(',')
                                resources[entry] = {
                                    "Type": "AWS::EC2::NetworkAclEntry",
                                    "Properties": {
                                        isIPv6NetACL(splitset[4]): splitset[4],
                                        "Egress": splitset[3],
                                        "NetworkAclId": {
                                            "Ref": networkacl
                                        },
                                        "PortRange": {
                                            "From": splitset[5],
                                            "To": splitset[6]
                                        },
                                        "Protocol": splitset[1],
                                        "RuleAction": splitset[2],
                                        "RuleNumber": splitset[0]
                                    }
                                }

                    if "NATGateways" in properties:
                        for natgw, objects in properties["NATGateways"].iteritems():
                            resources["EIP"+natgw] = {
                                "Type": "AWS::EC2::EIP",
                                "Properties": {
                                    "Domain": "vpc"
                                }
                            }

                            outputs["EIP"+natgw] = {
                                "Description": "EIP for " + natgw,
                                "Value": { 
                                    "Ref" : "EIP"+natgw 
                                },
                                "Export" : { 
                                    "Name" : {
                                        "Fn::Sub": "${AWS::StackName}-EIP-"+natgw 
                                    }
                                }
                            }
                            
                            resources[natgw] = {
                                "Type": "AWS::EC2::NatGateway",
                                "Properties": {
                                    "AllocationId": {
                                        "Fn::GetAtt": [
                                            "EIP"+natgw,
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

                            outputs[natgw] = {
                                "Description": natgw,
                                "Value": { 
                                    "Ref" : natgw 
                                },
                                "Export" : { 
                                    "Name" : {
                                        "Fn::Sub": "${AWS::StackName}-NATGW-"+natgw 
                                    }
                                }
                            }
                            
                            resources["Route"+natgw] = {
                                "Type": "AWS::EC2::Route",
                                "Properties": {
                                    "DestinationCidrBlock": "0.0.0.0/0",
                                    "NatGatewayId": {
                                        "Ref": natgw
                                    },
                                    "RouteTableId": {
                                        "Ref": objects["Routetable"]
                                    }
                                }
                            }
                            if "IPv6" in properties["Details"]:
                                if properties["Details"]["IPv6"]:
                                    resources["Route"+natgw+"IPv6"] = {
                                        "Type": "AWS::EC2::Route",
                                        "Properties": {
                                            "DestinationIpv6CidrBlock": "::/0",
                                            "EgressOnlyInternetGatewayId": {
                                                "Ref": "EgressGateway"
                                            },
                                            "RouteTableId": {
                                                "Ref": objects["Routetable"]
                                            }
                                        }
                                    }
                                    
                    if "SecurityGroups" in properties:
                        for secgroup, objects in properties["SecurityGroups"].iteritems():
                            resources[secgroup] = {
                                "Type" : "AWS::EC2::SecurityGroup",
                                "Properties" : {
                                    "GroupName": secgroup,
                                    "GroupDescription" : objects["GroupDescription"],
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }

                            if "SecurityGroupIngress" in objects:
                                resources[secgroup]["Properties"]["SecurityGroupIngress"] = []
                                for rule in objects["SecurityGroupIngress"]:
                                    resources[secgroup]["Properties"]["SecurityGroupIngress"].append({
                                            "IpProtocol" : rule[0],
                                            "FromPort" : rule[1],
                                            "ToPort" : rule[2],
                                            "CidrIp" : rule[3],
                                            "Description" : rule[4]
                                        })

                            if "SecurityGroupEgress" in objects:
                                resources[secgroup]["Properties"]["SecurityGroupEgress"] = []
                                for rule in objects["SecurityGroupEgress"]:
                                    resources[secgroup]["Properties"]["SecurityGroupEgress"].append({
                                            "IpProtocol" : rule[0],
                                            "FromPort" : rule[1],
                                            "ToPort" : rule[2],
                                            "CidrIp" : rule[3],
                                            "Description" : rule[4]
                                        })
                            if "Tags" in objects:
                                resources[secgroup]["Properties"]["Tags"] = []
                                for k,v in objects["Tags"].iteritems():
                                    resources[secgroup]["Properties"]["Tags"].append({
                                        "Key" : k,
                                        "Value" : v
                                        })

                    if "Endpoints" in properties:
                        for endpoint, objects in properties["Endpoints"].iteritems():
                            santisedendpoint = endpoint.replace("-", "").replace(".", "")
                            resources[santisedendpoint+"EndPoint"] = {
                                "Type": "AWS::EC2::VPCEndpoint",
                                "Properties": {
                                    "ServiceName": { "Fn::Join": [ "", [ "com.amazonaws.", { "Ref": "AWS::Region" }, "."+endpoint ] ] },
                                    "VpcEndpointType": objects["Type"],
                                    "VpcId": {
                                        "Ref": properties["Details"]["VPCName"]
                                    }
                                }
                            }

                            if objects["Type"] == "Gateway":
                                if "PolicyDocument" in objects:
                                    resources[santisedendpoint+"EndPoint"]["Properties"]["PolicyDocument"] = objects["PolicyDocument"]
                                if "RouteTableIds" in objects:
                                    resources[santisedendpoint+"EndPoint"]["Properties"]["RouteTableIds"] = []
                                    for routetable in objects["RouteTableIds"]:
                                        resources[santisedendpoint+"EndPoint"]["Properties"]["RouteTableIds"].append({"Ref": routetable })

                            if objects["Type"] == "Interface":
                                resources[santisedendpoint+"EndPoint"]["Properties"]["PrivateDnsEnabled"] = True
                                if "SubnetIds" in objects:
                                    resources[santisedendpoint+"EndPoint"]["Properties"]["SubnetIds"] = []
                                    for subnet in objects["SubnetIds"]:
                                        resources[santisedendpoint+"EndPoint"]["Properties"]["SubnetIds"].append({"Ref": subnet })
                                if "SecurityGroupIds" in objects:
                                    resources[santisedendpoint+"EndPoint"]["Properties"]["SecurityGroupIds"] = []
                                    for secgroup in objects["SecurityGroupIds"]:
                                        resources[santisedendpoint+"EndPoint"]["Properties"]["SecurityGroupIds"].append({"Ref": secgroup })
                                    
        response["Resources"] = resources
        response["Outputs"] = outputs
        macro_response["fragment"] = response
    except Exception as e:
        traceback.print_exc()
        macro_response["status"] = "failure"
        macro_response["errorMessage"] = str(e)

    print(json.dumps(macro_response))
    return macro_response