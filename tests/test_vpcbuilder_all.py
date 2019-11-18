import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderCoreLogicSetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = 10


class TestVPCBuilderCoreLogic(TestVPCBuilderCoreLogicSetup):

    def test_macro_all_objects(self):

        transform_call = {
            "transformId": "801604450668::VPC",
            "templateParameterValues": {
                "VGW": "vgw-06bbcf429c1cb0eed"
            },
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "VPC": {
                        "Type": "Versent::Network::VPC",
                        "Properties": {
                            "Subnets": {
                                "ReservedMgmt1": {
                                    "CIDR": "172.16.0.0/26",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 0
                                },
                                "ReservedMgmt2": {
                                    "CIDR": "172.16.1.0/26",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 1
                                },
                                "ReservedMgmt3": {
                                    "CIDR": "172.16.2.0/26",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 2
                                },
                                "Internal1": {
                                    "CIDR": "172.16.3.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 6
                                },
                                "Internal2": {
                                    "CIDR": "172.16.4.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 7
                                },
                                "Internal3": {
                                    "CIDR": "172.16.5.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 8
                                },
                                "ReservedNet3": {
                                    "CIDR": "172.16.2.192/26",
                                    "AZ": 2,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 9
                                },
                                "ReservedNet2": {
                                    "CIDR": "172.16.1.192/26",
                                    "AZ": 1,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 10
                                },
                                "ReservedNet1": {
                                    "CIDR": "172.16.0.192/26",
                                    "AZ": 0,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 11
                                },
                                "PerimeterInternal1": {
                                    "CIDR": "172.16.6.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 3
                                },
                                "PerimeterInternal2": {
                                    "CIDR": "172.16.7.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 4
                                },
                                "PerimeterInternal3": {
                                    "CIDR": "172.16.8.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 5
                                }
                            },
                            "TransitGateways": {
                                "Test1": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-01234567890123456",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW1",
                                        "Purpose": "Gateway Attach 1"
                                    }
                                },
                                "Test2": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-98765432109876543",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW2",
                                        "Purpose": "Gateway Attach 2"
                                    },
                                    "RouteTables": {
                                        "InternalRT1": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ],
                                        "InternalRT2": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ],
                                        "InternalRT3": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ]
                                    }
                                }
                            },
                            "Tags": {
                                "Name": "PRIVATE-EGRESS-VPC",
                                "Template": "VPC for private endpoints egress only"
                            },
                            "NATGateways": {
                                "NATGW3": {
                                    "Subnet": "ReservedNet3",
                                    "Routetable": "InternalRT3"
                                },
                                "NATGW2": {
                                    "Subnet": "ReservedNet2",
                                    "Routetable": "InternalRT2"
                                },
                                "NATGW1": {
                                    "Subnet": "ReservedNet1",
                                    "Routetable": "InternalRT1"
                                }
                            },
                            "NetworkACLs": {
                                "InternalSubnetAcl": {
                                    "InternalSubnetAclEntryOutTCPUnreserved": "106,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNSIPv6": "113,17,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutUDPUnreserved": "107,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOut": "100,-1,allow,true,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryOutSSH": "150,6,allow,true,0.0.0.0/0,22,22",
                                    "InternalSubnetAclEntryInUDPUnreservedIPv6": "105,17,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutTCPDNSIPv6": "112,6,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutTCPDNS": "110,6,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryOutHTTPS": "103,6,allow,true,0.0.0.0/0,443,443",
                                    "InternalSubnetAclEntryOutHTTP": "102,6,allow,true,0.0.0.0/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "InternalSubnetAclEntryInTCPUnreservedIPv6": "104,6,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNS": "111,17,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryIn": "100,-1,allow,false,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryInTCPUnreserved": "102,6,allow,false,0.0.0.0/0,1024,65535",
                                    "InternalSubnetAclEntryInUDPUnreserved": "103,17,allow,false,0.0.0.0/0,1024,65535"
                                },
                                "RestrictedSubnetAcl": {
                                    "RestrictedSubnetAclEntryInUDPUnReserved": "91,17,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutSSH": "103,6,allow,true,0.0.0.0/0,22,22",
                                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": "151,6,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": "92,6,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryNTP": "120,6,allow,true,0.0.0.0/0,123,123",
                                    "RestrictedSubnetAclEntryOutPuppet": "94,6,allow,true,172.16.0.0/16,8140,8140",
                                    "RestrictedSubnetAclEntryIn": "110,-1,allow,false,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTP": "101,6,allow,true,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPSIPv6": "104,6,allow,false,::/0,443,443",
                                    "RestrictedSubnetAclEntryInNetBios": "170,6,allow,false,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutDNSTCP": "150,6,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": "93,17,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryInHTTP": "101,6,allow,false,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPIPv6": "103,6,allow,false,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutDNSUDP": "160,17,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInTCPUnReserved": "90,6,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutTCPUnReserved": "90,6,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInDNSTCP": "150,6,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": "93,17,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutNetBios1": "180,6,allow,true,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOut": "110,-1,allow,true,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutHTTPS": "102,6,allow,true,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryOutNetBios": "170,6,allow,true,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": "92,6,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutUDPUnReserved": "91,17,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInNetBios1": "80,6,allow,false,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOutSSHIPv6": "106,6,allow,true,::/0,22,22",
                                    "RestrictedSubnetAclEntryInHTTPS": "102,6,allow,false,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryInDNSUDP": "160,17,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": "161,17,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryInSquid2": "140,6,allow,false,172.16.0.0/16,3128,3128"
                                }
                            },
                            "SecurityGroups": {
                                "VPCEndpoint": {
                                    "SecurityGroupIngress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ],
                                    "Tags": {
                                        "Name": "VPCEndpoint"
                                    },
                                    "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                                    "SecurityGroupEgress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ]
                                }
                            },
                            "Details": {
                                "VPCDesc": "Private Egress VPC",
                                "Region": "ap-southeast-2",
                                "VPCName": "PRIVATEEGRESSVPC",
                                "IPv6": "true"
                            },
                            "DHCP": {
                                "NTPServers": "169.254.169.123",
                                "NTBType": 2,
                                "Name": "DhcpOptions",
                                "DNSServers": "172.16.0.2"
                            },
                            "CIDR": "172.16.0.0/20",
                            "Endpoints": {
                                "kinesis-streams": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudtrail": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudformation": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "elasticloadbalancing": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ec2": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "logs": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "monitoring": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "s3": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "dynamodb": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "ec2messages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "kms": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "config": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "events": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssm": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sns": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.runtime": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "codebuild": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "servicecatalog": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "execute-api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "secretsmanager": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssmmessages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                }
                            },
                            "RouteTables": {
                                "InternalRT3": "",
                                "PublicRT": [
                                    {
                                        "RouteName": "PublicRoute",
                                        "RouteCIDR": "0.0.0.0/0",
                                        "RouteGW": "InternetGateway"
                                    },
                                    {
                                        "RouteName": "PublicRouteIPv6",
                                        "RouteCIDR": "::/0",
                                        "RouteGW": "InternetGateway"
                                    }
                                ],
                                "InternalRT2": "",
                                "InternalRT1": ""
                            }
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "Mappings": {}
            },
            "region": "us-east-1",
            "params": {},
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "accountId": "012345678901"
        }
        test_assert = {
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "status": "success",
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "PRIVATEEGRESSVPC": {
                        "Type": "AWS::EC2::VPC",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/20",
                            "EnableDnsHostnames": True,
                            "EnableDnsSupport": True,
                            "InstanceTenancy": "default",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATEEGRESSVPC"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "IPv6Block": {
                        "Type": "AWS::EC2::VPCCidrBlock",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AmazonProvidedIpv6CidrBlock": True
                        }
                    },
                    "EgressGateway": {
                        "Type": "AWS::EC2::EgressOnlyInternetGateway",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "DhcpOptions": {
                        "Type": "AWS::EC2::DHCPOptions",
                        "Properties": {
                            "DomainNameServers": [
                                "172.16.0.2"
                            ],
                            "NtpServers": [
                                "169.254.169.123"
                            ],
                            "NetbiosNodeType": 2,
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "DhcpOptions"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "DhcpOptionsAssociation": {
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
                        "Properties": {
                            "DhcpOptionsId": {
                                "Ref": "DhcpOptions"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternetGateway": {
                        "Type": "AWS::EC2::InternetGateway",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternetGateway"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "IGWVPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "VPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        }
                    },
                    "VPCFlowLogsRole": {
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
                    },
                    "VPCFlowLogs": {
                        "Type": "AWS::EC2::FlowLog",
                        "Properties": {
                            "DeliverLogsPermissionArn": {
                                "Fn::GetAtt": [
                                    "VPCFlowLogsRole",
                                    "Arn"
                                ]
                            },
                            "LogGroupName": "FlowLogsGroup",
                            "ResourceId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "ResourceType": "VPC",
                            "TrafficType": "ALL"
                        }
                    },
                    "Test1TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-01234567890123456",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Internal1"
                                },
                                {
                                    "Ref": "Internal2"
                                },
                                {
                                    "Ref": "Internal3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW1"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "Test2TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-98765432109876543",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Internal1"
                                },
                                {
                                    "Ref": "Internal2"
                                },
                                {
                                    "Ref": "Internal3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW2"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "Test2InternalRT1Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT1Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT2Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT2Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT3Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT3Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "InternalRT3": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalRT3RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "InternalRT3"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "PublicRT": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PublicRT"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "PublicRTRoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "PublicRoute": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "PublicRouteIPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "InternalRT2": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalRT2RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "InternalRT2"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "InternalRT1": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalRT1RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "InternalRT1"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "ReservedMgmt1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        }
                    },
                    "ReservedMgmt3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        }
                    },
                    "Internal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.3.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    6,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        }
                    },
                    "Internal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        }
                    },
                    "Internal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.4.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    7,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        }
                    },
                    "Internal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        }
                    },
                    "Internal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.5.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    8,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        }
                    },
                    "Internal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        }
                    },
                    "ReservedNet3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    9,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    10,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    11,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        }
                    },
                    "ReservedNet1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        }
                    },
                    "PerimeterInternal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.6.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    3,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.7.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    4,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.8.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    5,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        }
                    },
                    "PerimeterInternal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 113
                        }
                    },
                    "InternalSubnetAclEntryOutUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 107
                        }
                    },
                    "InternalSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 112
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "InternalSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 111
                        }
                    },
                    "InternalSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "RestrictedSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 151
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryNTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 123,
                                "To": 123
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 120
                        }
                    },
                    "RestrictedSubnetAclEntryOutPuppet": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 8140,
                                "To": 8140
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 94
                        }
                    },
                    "RestrictedSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 180
                        }
                    },
                    "RestrictedSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 80
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSHIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 161
                        }
                    },
                    "RestrictedSubnetAclEntryInSquid2": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 3128,
                                "To": 3128
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 140
                        }
                    },
                    "EIPNATGW3": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW3": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW3",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT3NATGW3": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "InternalRT3NATGW3IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW2": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW2",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT2NATGW2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "InternalRT2NATGW2IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW1": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW1",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT1NATGW1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "InternalRT1NATGW1IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "VPCEndpoint": {
                        "Type": "AWS::EC2::SecurityGroup",
                        "Properties": {
                            "GroupName": "VPCEndpoint",
                            "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SecurityGroupIngress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "SecurityGroupEgress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "VPCEndpoint"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "kinesisstreamsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kinesis-streams"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudtrailEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudtrail"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudformationEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudformation"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "elasticloadbalancingEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".elasticloadbalancing"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ec2EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "logsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".logs"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "monitoringEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".monitoring"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "s3EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".s3"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "InternalRT1"
                                },
                                {
                                    "Ref": "InternalRT2"
                                },
                                {
                                    "Ref": "InternalRT3"
                                }
                            ]
                        }
                    },
                    "dynamodbEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".dynamodb"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "InternalRT1"
                                },
                                {
                                    "Ref": "InternalRT2"
                                },
                                {
                                    "Ref": "InternalRT3"
                                }
                            ]
                        }
                    },
                    "ec2messagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2messages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "kmsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kms"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "configEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".config"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "eventsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".events"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssm"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "snsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sns"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerruntimeEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.runtime"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "codebuildEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".codebuild"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "servicecatalogEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".servicecatalog"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "executeapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".execute-api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "secretsmanagerEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".secretsmanager"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmmessagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssmmessages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "Mappings": {},
                "Outputs": {
                    "PRIVATEEGRESSVPC": {
                        "Description": "PRIVATEEGRESSVPC",
                        "Value": {
                            "Ref": "PRIVATEEGRESSVPC"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-VPCid"
                            }
                        }
                    },
                    "InternalRT3": {
                        "Description": "InternalRT3",
                        "Value": {
                            "Ref": "InternalRT3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT3"
                            }
                        }
                    },
                    "PublicRT": {
                        "Description": "PublicRT",
                        "Value": {
                            "Ref": "PublicRT"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PublicRT"
                            }
                        }
                    },
                    "InternalRT2": {
                        "Description": "InternalRT2",
                        "Value": {
                            "Ref": "InternalRT2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT2"
                            }
                        }
                    },
                    "InternalRT1": {
                        "Description": "InternalRT1",
                        "Value": {
                            "Ref": "InternalRT1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT1"
                            }
                        }
                    },
                    "ReservedMgmt1": {
                        "Description": "ReservedMgmt1",
                        "Value": {
                            "Ref": "ReservedMgmt1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt2": {
                        "Description": "ReservedMgmt2",
                        "Value": {
                            "Ref": "ReservedMgmt2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt3": {
                        "Description": "ReservedMgmt3",
                        "Value": {
                            "Ref": "ReservedMgmt3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt3"
                            }
                        }
                    },
                    "Internal1": {
                        "Description": "Internal1",
                        "Value": {
                            "Ref": "Internal1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal1"
                            }
                        }
                    },
                    "Internal2": {
                        "Description": "Internal2",
                        "Value": {
                            "Ref": "Internal2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal2"
                            }
                        }
                    },
                    "Internal3": {
                        "Description": "Internal3",
                        "Value": {
                            "Ref": "Internal3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal3"
                            }
                        }
                    },
                    "ReservedNet3": {
                        "Description": "ReservedNet3",
                        "Value": {
                            "Ref": "ReservedNet3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet2": {
                        "Description": "ReservedNet2",
                        "Value": {
                            "Ref": "ReservedNet2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet1": {
                        "Description": "ReservedNet1",
                        "Value": {
                            "Ref": "ReservedNet1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet1"
                            }
                        }
                    },
                    "PerimeterInternal1": {
                        "Description": "PerimeterInternal1",
                        "Value": {
                            "Ref": "PerimeterInternal1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal2": {
                        "Description": "PerimeterInternal2",
                        "Value": {
                            "Ref": "PerimeterInternal2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal3": {
                        "Description": "PerimeterInternal3",
                        "Value": {
                            "Ref": "PerimeterInternal3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Description": "InternalSubnetAcl",
                        "Value": {
                            "Ref": "InternalSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-InternalSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Description": "RestrictedSubnetAcl",
                        "Value": {
                            "Ref": "RestrictedSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-RestrictedSubnetAcl"
                            }
                        }
                    },
                    "EIPNATGW3": {
                        "Description": "EIP for NATGW3",
                        "Value": {
                            "Ref": "EIPNATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW3"
                            }
                        }
                    },
                    "NATGW3": {
                        "Description": "NATGW3",
                        "Value": {
                            "Ref": "NATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW3"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Description": "EIP for NATGW2",
                        "Value": {
                            "Ref": "EIPNATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW2"
                            }
                        }
                    },
                    "NATGW2": {
                        "Description": "NATGW2",
                        "Value": {
                            "Ref": "NATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Description": "EIP for NATGW1",
                        "Value": {
                            "Ref": "EIPNATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW1"
                            }
                        }
                    },
                    "NATGW1": {
                        "Description": "NATGW1",
                        "Value": {
                            "Ref": "NATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW1"
                            }
                        }
                    }
                }
            }
        }
        actual = src.macro.handler(transform_call, "")
        print(json.dumps(actual))
        self.assertEquals(test_assert, actual)

    def test_macro_all_objects_by_ref(self):

        transform_call = {
            "transformId": "801604450668::VPC",
            "templateParameterValues": {
                "VGW": "vgw-06bbcf429c1cb0eed",
                "Environment": "Dev",
                "VpcCidr": "10.0.0.0/20",
                "DnsServer": "10.0.0.2",
                "PublicCidr1": "10.0.0.0/24",
                "PublicCidr2": "10.0.0.1/24",
                "PublicCidr3": "10.0.0.2/24",
                "PrivateCidr1": "10.0.0.3/24",
                "PrivateCidr2": "10.0.0.4/24",
                "PrivateCidr3": "10.0.0.5/24",
                "ProtectedCidr1": "10.0.0.6/24",
                "ProtectedCidr2": "10.0.0.7/24",
                "ProtectedCidr3": "10.0.0.8/24",
            },
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "VPC": {
                        "Type": "Versent::Network::VPC",
                        "Properties": {
                            "Subnets": {
                                "Public1": {
                                    "CIDR": {
                                        "Ref": "PublicCidr1"
                                    },
                                    "AZ": 0,
                                    "NetACL": "PublicSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 0
                                },
                                "Public2": {
                                    "CIDR": {
                                        "Ref": "PublicCidr2"
                                    },
                                    "AZ": 1,
                                    "NetACL": "PublicSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 1
                                },
                                "Public3": {
                                    "CIDR": {
                                        "Ref": "PublicCidr3"
                                    },
                                    "AZ": 2,
                                    "NetACL": "PublicSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 2
                                },
                                "Private1": {
                                    "CIDR": {
                                        "Ref": "PrivateCidr1"
                                    },
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "PrivateRT1",
                                    "IPv6Iter": 0
                                },
                                "Private2": {
                                    "CIDR": {
                                        "Ref": "PrivateCidr2"
                                    },
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "PrivateRT2",
                                    "IPv6Iter": 1
                                },
                                "Private3": {
                                    "CIDR": {
                                        "Ref": "PrivateCidr3"
                                    },
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "PrivateRT3",
                                    "IPv6Iter": 2
                                },
                                "Protected1": {
                                    "CIDR": {
                                        "Ref": "ProtectedCidr1"
                                    },
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "RestrictedRT",
                                    "IPv6Iter": 0
                                },
                                "Protected2": {
                                    "CIDR": {
                                        "Ref": "ProtectedCidr2"
                                    },
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "RestrictedRT",
                                    "IPv6Iter": 1
                                },
                                "Protected3": {
                                    "CIDR": {
                                        "Ref": "ProtectedCidr3"
                                    },
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "RestrictedRT",
                                    "IPv6Iter": 2
                                }
                            },
                            "TransitGateways": {
                                "Test1": {
                                    "Subnets": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "TransitGatewayId": "tgw-01234567890123456",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW1",
                                        "Purpose": "Gateway Attach 1"
                                    }
                                },
                                "Test2": {
                                    "Subnets": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "TransitGatewayId": "tgw-98765432109876543",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW2",
                                        "Purpose": "Gateway Attach 2"
                                    }
                                }
                            },
                            "Tags": {
                                "Name": "PRIVATE-EGRESS-VPC",
                                "Template": "VPC for private endpoints egress only",
                                "info:environment": "Staging",
                                "info:owner": "Versent"
                            },
                            "NATGateways": {
                                "NATGW3": {
                                    "Subnet": "Public1",
                                    "Routetable": "PrivateRT1"
                                },
                                "NATGW2": {
                                    "Subnet": "Public2",
                                    "Routetable": "PrivateRT2"
                                },
                                "NATGW1": {
                                    "Subnet": "Public3",
                                    "Routetable": "PrivateRT3"
                                }
                            },
                            "NetworkACLs": {
                                "InternalSubnetAcl": {
                                    "InternalSubnetAclEntryOutTCPUnreserved": "106,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNSIPv6": "113,17,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutUDPUnreserved": "107,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOut": "100,-1,allow,true,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryOutSSH": "150,6,allow,true,0.0.0.0/0,22,22",
                                    "InternalSubnetAclEntryInUDPUnreservedIPv6": "105,17,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutTCPDNSIPv6": "112,6,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutTCPDNS": "110,6,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryOutHTTPS": "103,6,allow,true,0.0.0.0/0,443,443",
                                    "InternalSubnetAclEntryOutHTTP": "102,6,allow,true,0.0.0.0/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "InternalSubnetAclEntryInTCPUnreservedIPv6": "104,6,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNS": "111,17,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryIn": "100,-1,allow,false,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryInTCPUnreserved": "102,6,allow,false,0.0.0.0/0,1024,65535",
                                    "InternalSubnetAclEntryInUDPUnreserved": "103,17,allow,false,0.0.0.0/0,1024,65535"
                                },
                                "PublicSubnetAcl": {
                                    "RestrictedSubnetAclEntryInUDPUnReserved": "91,17,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutSSH": "103,6,allow,true,0.0.0.0/0,22,22",
                                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": "151,6,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": "92,6,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryNTP": "120,6,allow,true,0.0.0.0/0,123,123",
                                    "RestrictedSubnetAclEntryOutPuppet": "94,6,allow,true,172.16.0.0/16,8140,8140",
                                    "RestrictedSubnetAclEntryIn": "110,-1,allow,false,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTP": "101,6,allow,true,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPSIPv6": "104,6,allow,false,::/0,443,443",
                                    "RestrictedSubnetAclEntryInNetBios": "170,6,allow,false,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutDNSTCP": "150,6,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": "93,17,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryInHTTP": "101,6,allow,false,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPIPv6": "103,6,allow,false,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutDNSUDP": "160,17,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInTCPUnReserved": "90,6,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutTCPUnReserved": "90,6,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInDNSTCP": "150,6,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": "93,17,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutNetBios1": "180,6,allow,true,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOut": "110,-1,allow,true,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutHTTPS": "102,6,allow,true,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryOutNetBios": "170,6,allow,true,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": "92,6,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutUDPUnReserved": "91,17,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInNetBios1": "80,6,allow,false,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOutSSHIPv6": "106,6,allow,true,::/0,22,22",
                                    "RestrictedSubnetAclEntryInHTTPS": "102,6,allow,false,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryInDNSUDP": "160,17,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": "161,17,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryInSquid2": "140,6,allow,false,172.16.0.0/16,3128,3128"
                                }
                            },
                            "SecurityGroups": {
                                "VPCEndpoint": {
                                    "SecurityGroupIngress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ],
                                    "Tags": {
                                        "Name": "VPCEndpoint"
                                    },
                                    "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                                    "SecurityGroupEgress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ]
                                }
                            },
                            "Details": {
                                "VPCDesc": "PrivateVPC",
                                "Region": "ap-southeast-2",
                                "VPCName": {
                                    "Fn::Sub": "VPC${Environment}"
                                },
                                "IPv6": "false"
                            },
                            "DHCP": {
                                "NTPServers": "169.254.169.123",
                                "NTBType": 2,
                                "Name": "DhcpOptions",
                                "DNSServers": "172.16.0.2"
                            },
                            "CIDR": "172.16.0.0/20",
                            "Endpoints": {
                                "kinesis-streams": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudtrail": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudformation": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "elasticloadbalancing": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ec2": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "logs": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "monitoring": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "s3": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "PrivateRT1",
                                        "PrivateRT2",
                                        "PrivateRT3",
                                        "RestrictedRT"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "dynamodb": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "PrivateRT1",
                                        "PrivateRT2",
                                        "PrivateRT3",
                                        "RestrictedRT"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "ec2messages": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "kms": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "config": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "events": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.api": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssm": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sns": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.runtime": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "codebuild": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "servicecatalog": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "execute-api": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "secretsmanager": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssmmessages": {
                                    "SubnetIds": [
                                        "Private1",
                                        "Private2",
                                        "Private3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                }
                            },
                            "RouteTables": {
                                "PrivateRT3": "",
                                "PublicRT": [
                                    {
                                        "RouteName": "PublicRoute",
                                        "RouteCIDR": "0.0.0.0/0",
                                        "RouteGW": "InternetGateway"
                                    }
                                ],
                                "PrivateRT2": "",
                                "PrivateRT1": "",
                                "RestrictedRT": ""
                            }
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    },
                    "Environment": {
                        "Description": "Name of target environment",
                        "Type": "String",
                        "Default": "foo"
                    },
                    "VpcCidr": {
                        "Description": "CIDR range for the complete VPC",
                        "Type": "String",
                        "Default": "10.0.0.0/20",
                    },
                    "DnsServer": {
                        "Description": "DNS server",
                        "Type": "String",
                        "Default": "10.0.0.2"
                    },
                    "PublicCidr1": {
                        "Description": "CIDR range for Public1",
                        "Type": "String",
                        "Default": "10.0.0.0/24"
                    },
                    "PublicCidr2": {
                        "Description": "CIDR range for Public2",
                        "Type": "String",
                        "Default": "10.0.0.1/24"
                    },
                    "PublicCidr3": {
                        "Description": "CIDR range for Public3",
                        "Type": "String",
                        "Default": "10.0.0.2/24"
                    },
                    "PrivateCidr1": {
                        "Description": "CIDR range for Private1",
                        "Type": "String",
                        "Default": "10.0.0.3/24"
                    },
                    "PrivateCidr2": {
                        "Description": "CIDR range for Private2",
                        "Type": "String",
                        "Default": "10.0.0.4/24"
                    },
                    "PrivateCidr3": {
                        "Description": "CIDR range for Private3",
                        "Type": "String",
                        "Default": "10.0.0.5/24"
                    },
                    "ProtectedCidr1": {
                        "Description": "CIDR range for Protected1",
                        "Type": "String",
                        "Default": "10.0.0.6/24"
                    },
                    "ProtectedCidr2": {
                        "Description": "CIDR range for Protected2",
                        "Type": "String",
                        "Default": "10.0.0.7/24"
                    },
                    "ProtectedCidr3": {
                        "Description": "CIDR range for Protected3",
                        "Type": "String",
                        "Default": "10.0.0.8/24"
                    }
                },
                "Mappings": {}
            },
            "region": "us-east-1",
            "params": {},
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "accountId": "012345678901"
        }
        test_assert = {
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "status": "success",
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "VPCDev": {
                        "Type": "AWS::EC2::VPC",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/20",
                            "EnableDnsHostnames": True,
                            "EnableDnsSupport": True,
                            "InstanceTenancy": "default",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "VPCDev"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "IPv6Block": {
                        "Type": "AWS::EC2::VPCCidrBlock",
                        "Properties": {
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AmazonProvidedIpv6CidrBlock": True
                        }
                    },
                    "EgressGateway": {
                        "Type": "AWS::EC2::EgressOnlyInternetGateway",
                        "Properties": {
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "DhcpOptions": {
                        "Type": "AWS::EC2::DHCPOptions",
                        "Properties": {
                            "DomainNameServers": [
                                "172.16.0.2"
                            ],
                            "NtpServers": [
                                "169.254.169.123"
                            ],
                            "NetbiosNodeType": 2,
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "DhcpOptions"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "DhcpOptionsAssociation": {
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
                        "Properties": {
                            "DhcpOptionsId": {
                                "Ref": "DhcpOptions"
                            },
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "InternetGateway": {
                        "Type": "AWS::EC2::InternetGateway",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternetGateway"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "IGWVPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "VPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        }
                    },
                    "VPCFlowLogsRole": {
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
                    },
                    "VPCFlowLogs": {
                        "Type": "AWS::EC2::FlowLog",
                        "Properties": {
                            "DeliverLogsPermissionArn": {
                                "Fn::GetAtt": [
                                    "VPCFlowLogsRole",
                                    "Arn"
                                ]
                            },
                            "LogGroupName": "FlowLogsGroup",
                            "ResourceId": {
                                "Ref": "VPCDev"
                            },
                            "ResourceType": "VPC",
                            "TrafficType": "ALL"
                        }
                    },
                    "Test1TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-01234567890123456",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW1"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "Test2TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-98765432109876543",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW2"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "PrivateRT3": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PrivateRT3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "PrivateRT3RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "PrivateRT3"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "PublicRT": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PublicRT"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "PublicRTRoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "PublicRoute": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "PrivateRT2": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PrivateRT2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "PrivateRT2RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "PrivateRT2"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "PrivateRT1": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PrivateRT1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "PrivateRT1RoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "PrivateRT1"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "RestrictedRT": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "RestrictedRT"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "RestrictedRTRoutePropagation": {
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation",
                        "Properties": {
                            "RouteTableIds": [
                                {
                                    "Ref": "RestrictedRT"
                                }
                            ],
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ]
                    },
                    "Public1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PublicCidr1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Public1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Public1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "Public1"
                            }
                        }
                    },
                    "Public1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Public1"
                            }
                        }
                    },
                    "Public2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PublicCidr2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Public2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Public2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "Public2"
                            }
                        }
                    },
                    "Public2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Public2"
                            }
                        }
                    },
                    "Public3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PublicCidr3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Public3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Public3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "Public3"
                            }
                        }
                    },
                    "Public3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Public3"
                            }
                        }
                    },
                    "Private1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PrivateCidr1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Private1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Private1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PrivateRT1"
                            },
                            "SubnetId": {
                                "Ref": "Private1"
                            }
                        }
                    },
                    "Private1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Private1"
                            }
                        }
                    },
                    "Private2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PrivateCidr2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Private2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Private2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PrivateRT2"
                            },
                            "SubnetId": {
                                "Ref": "Private2"
                            }
                        }
                    },
                    "Private2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Private2"
                            }
                        }
                    },
                    "Private3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "PrivateCidr3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Private3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Private3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PrivateRT3"
                            },
                            "SubnetId": {
                                "Ref": "Private3"
                            }
                        }
                    },
                    "Private3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Private3"
                            }
                        }
                    },
                    "Protected1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "ProtectedCidr1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Protected1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Protected1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "RestrictedRT"
                            },
                            "SubnetId": {
                                "Ref": "Protected1"
                            }
                        }
                    },
                    "Protected1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Protected1"
                            }
                        }
                    },
                    "Protected2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "ProtectedCidr2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Protected2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Protected2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "RestrictedRT"
                            },
                            "SubnetId": {
                                "Ref": "Protected2"
                            }
                        }
                    },
                    "Protected2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Protected2"
                            }
                        }
                    },
                    "Protected3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": {
                                "Ref": "ProtectedCidr3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Protected3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "VPCDev",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            9,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Protected3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "RestrictedRT"
                            },
                            "SubnetId": {
                                "Ref": "Protected3"
                            }
                        }
                    },
                    "Protected3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Protected3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 113
                        }
                    },
                    "InternalSubnetAclEntryOutUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 107
                        }
                    },
                    "InternalSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 112
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "InternalSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 111
                        }
                    },
                    "InternalSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "PublicSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PublicSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ],
                            "VpcId": {
                                "Ref": "VPCDev"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 151
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryNTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 123,
                                "To": 123
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 120
                        }
                    },
                    "RestrictedSubnetAclEntryOutPuppet": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 8140,
                                "To": 8140
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 94
                        }
                    },
                    "RestrictedSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 180
                        }
                    },
                    "RestrictedSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 80
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSHIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 161
                        }
                    },
                    "RestrictedSubnetAclEntryInSquid2": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "PublicSubnetAcl"
                            },
                            "PortRange": {
                                "From": 3128,
                                "To": 3128
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 140
                        }
                    },
                    "EIPNATGW3": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW3": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW3",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "Public1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "PrivateRT1NATGW3": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW3"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT1"
                            }
                        }
                    },
                    "PrivateRT1NATGW3IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT1"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW2": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW2",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "Public2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "PrivateRT2NATGW2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW2"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT2"
                            }
                        }
                    },
                    "PrivateRT2NATGW2IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW1": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW1",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "Public3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "PrivateRT3NATGW1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW1"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT3"
                            }
                        }
                    },
                    "PrivateRT3NATGW1IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PrivateRT3"
                            }
                        }
                    },
                    "VPCEndpoint": {
                        "Type": "AWS::EC2::SecurityGroup",
                        "Properties": {
                            "GroupName": "VPCEndpoint",
                            "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "SecurityGroupIngress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "SecurityGroupEgress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "VPCEndpoint"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                },
                                {
                                    "Key": "info:environment",
                                    "Value": "Staging"
                                },
                                {
                                    "Key": "info:owner",
                                    "Value": "Versent"
                                }
                            ]
                        }
                    },
                    "kinesisstreamsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kinesis-streams"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudtrailEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudtrail"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudformationEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudformation"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "elasticloadbalancingEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".elasticloadbalancing"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ec2EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "logsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".logs"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "monitoringEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".monitoring"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "s3EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".s3"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "PrivateRT1"
                                },
                                {
                                    "Ref": "PrivateRT2"
                                },
                                {
                                    "Ref": "PrivateRT3"
                                },
                                {
                                    "Ref": "RestrictedRT"
                                }
                            ]
                        }
                    },
                    "dynamodbEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".dynamodb"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "PrivateRT1"
                                },
                                {
                                    "Ref": "PrivateRT2"
                                },
                                {
                                    "Ref": "PrivateRT3"
                                },
                                {
                                    "Ref": "RestrictedRT"
                                }
                            ]
                        }
                    },
                    "ec2messagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2messages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "kmsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kms"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "configEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".config"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "eventsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".events"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssm"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "snsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sns"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerruntimeEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.runtime"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "codebuildEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".codebuild"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "servicecatalogEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".servicecatalog"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "executeapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".execute-api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "secretsmanagerEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".secretsmanager"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmmessagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssmmessages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "VPCDev"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "Private1"
                                },
                                {
                                    "Ref": "Private2"
                                },
                                {
                                    "Ref": "Private3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    },
                    "Environment": {
                        "Description": "Name of target environment",
                        "Type": "String",
                        "Default": "foo"
                    },
                    "VpcCidr": {
                        "Description": "CIDR range for the complete VPC",
                        "Type": "String",
                        "Default": "10.0.0.0/20"
                    },
                    "DnsServer": {
                        "Description": "DNS server",
                        "Type": "String",
                        "Default": "10.0.0.2"
                    },
                    "PublicCidr1": {
                        "Description": "CIDR range for Public1",
                        "Type": "String",
                        "Default": "10.0.0.0/24"
                    },
                    "PublicCidr2": {
                        "Description": "CIDR range for Public2",
                        "Type": "String",
                        "Default": "10.0.0.1/24"
                    },
                    "PublicCidr3": {
                        "Description": "CIDR range for Public3",
                        "Type": "String",
                        "Default": "10.0.0.2/24"
                    },
                    "PrivateCidr1": {
                        "Description": "CIDR range for Private1",
                        "Type": "String",
                        "Default": "10.0.0.3/24"
                    },
                    "PrivateCidr2": {
                        "Description": "CIDR range for Private2",
                        "Type": "String",
                        "Default": "10.0.0.4/24"
                    },
                    "PrivateCidr3": {
                        "Description": "CIDR range for Private3",
                        "Type": "String",
                        "Default": "10.0.0.5/24"
                    },
                    "ProtectedCidr1": {
                        "Description": "CIDR range for Protected1",
                        "Type": "String",
                        "Default": "10.0.0.6/24"
                    },
                    "ProtectedCidr2": {
                        "Description": "CIDR range for Protected2",
                        "Type": "String",
                        "Default": "10.0.0.7/24"
                    },
                    "ProtectedCidr3": {
                        "Description": "CIDR range for Protected3",
                        "Type": "String",
                        "Default": "10.0.0.8/24"
                    }
                },
                "Mappings": {},
                "Outputs": {
                    "VPCDev": {
                        "Description": "VPCDev",
                        "Value": {
                            "Fn::Sub": "VPCDev"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-VPCid"
                            }
                        }
                    },
                    "PrivateRT3": {
                        "Description": "PrivateRT3",
                        "Value": {
                            "Ref": "PrivateRT3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PrivateRT3"
                            }
                        }
                    },
                    "PublicRT": {
                        "Description": "PublicRT",
                        "Value": {
                            "Ref": "PublicRT"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PublicRT"
                            }
                        }
                    },
                    "PrivateRT2": {
                        "Description": "PrivateRT2",
                        "Value": {
                            "Ref": "PrivateRT2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PrivateRT2"
                            }
                        }
                    },
                    "PrivateRT1": {
                        "Description": "PrivateRT1",
                        "Value": {
                            "Ref": "PrivateRT1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PrivateRT1"
                            }
                        }
                    },
                    "RestrictedRT": {
                        "Description": "RestrictedRT",
                        "Value": {
                            "Ref": "RestrictedRT"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-RestrictedRT"
                            }
                        }
                    },
                    "Public1": {
                        "Description": "Public1",
                        "Value": {
                            "Ref": "Public1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Public1"
                            }
                        }
                    },
                    "Public2": {
                        "Description": "Public2",
                        "Value": {
                            "Ref": "Public2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Public2"
                            }
                        }
                    },
                    "Public3": {
                        "Description": "Public3",
                        "Value": {
                            "Ref": "Public3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Public3"
                            }
                        }
                    },
                    "Private1": {
                        "Description": "Private1",
                        "Value": {
                            "Ref": "Private1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Private1"
                            }
                        }
                    },
                    "Private2": {
                        "Description": "Private2",
                        "Value": {
                            "Ref": "Private2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Private2"
                            }
                        }
                    },
                    "Private3": {
                        "Description": "Private3",
                        "Value": {
                            "Ref": "Private3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Private3"
                            }
                        }
                    },
                    "Protected1": {
                        "Description": "Protected1",
                        "Value": {
                            "Ref": "Protected1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Protected1"
                            }
                        }
                    },
                    "Protected2": {
                        "Description": "Protected2",
                        "Value": {
                            "Ref": "Protected2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Protected2"
                            }
                        }
                    },
                    "Protected3": {
                        "Description": "Protected3",
                        "Value": {
                            "Ref": "Protected3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Protected3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Description": "InternalSubnetAcl",
                        "Value": {
                            "Ref": "InternalSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-InternalSubnetAcl"
                            }
                        }
                    },
                    "PublicSubnetAcl": {
                        "Description": "PublicSubnetAcl",
                        "Value": {
                            "Ref": "PublicSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-PublicSubnetAcl"
                            }
                        }
                    },
                    "EIPNATGW3": {
                        "Description": "EIP for NATGW3",
                        "Value": {
                            "Ref": "EIPNATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW3"
                            }
                        }
                    },
                    "NATGW3": {
                        "Description": "NATGW3",
                        "Value": {
                            "Ref": "NATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW3"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Description": "EIP for NATGW2",
                        "Value": {
                            "Ref": "EIPNATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW2"
                            }
                        }
                    },
                    "NATGW2": {
                        "Description": "NATGW2",
                        "Value": {
                            "Ref": "NATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Description": "EIP for NATGW1",
                        "Value": {
                            "Ref": "EIPNATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW1"
                            }
                        }
                    },
                    "NATGW1": {
                        "Description": "NATGW1",
                        "Value": {
                            "Ref": "NATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW1"
                            }
                        }
                    }
                }
            }
        }
        actual = src.macro.handler(transform_call, "")
        self.assertEquals(test_assert, actual)

    def test_macro_all_objects_no_vpgw(self):

        transform_call = {
            "transformId": "801604450668::VPC",
            "templateParameterValues": {},
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "VPC": {
                        "Type": "Versent::Network::VPC",
                        "Properties": {
                            "Subnets": {
                                "ReservedMgmt1": {
                                    "CIDR": "172.16.0.0/26",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 0
                                },
                                "ReservedMgmt2": {
                                    "CIDR": "172.16.1.0/26",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 1
                                },
                                "ReservedMgmt3": {
                                    "CIDR": "172.16.2.0/26",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 2
                                },
                                "Internal1": {
                                    "CIDR": "172.16.3.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 6
                                },
                                "Internal2": {
                                    "CIDR": "172.16.4.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 7
                                },
                                "Internal3": {
                                    "CIDR": "172.16.5.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 8
                                },
                                "ReservedNet3": {
                                    "CIDR": "172.16.2.192/26",
                                    "AZ": 2,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 9
                                },
                                "ReservedNet2": {
                                    "CIDR": "172.16.1.192/26",
                                    "AZ": 1,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 10
                                },
                                "ReservedNet1": {
                                    "CIDR": "172.16.0.192/26",
                                    "AZ": 0,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT",
                                    "IPv6Iter": 11
                                },
                                "PerimeterInternal1": {
                                    "CIDR": "172.16.6.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1",
                                    "IPv6Iter": 3
                                },
                                "PerimeterInternal2": {
                                    "CIDR": "172.16.7.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2",
                                    "IPv6Iter": 4
                                },
                                "PerimeterInternal3": {
                                    "CIDR": "172.16.8.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3",
                                    "IPv6Iter": 5
                                }
                            },
                            "TransitGateways": {
                                "Test1": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-01234567890123456",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW1",
                                        "Purpose": "Gateway Attach 1"
                                    }
                                },
                                "Test2": {
                                    "Subnets": [
                                        "Internal1",
                                        "Internal2",
                                        "Internal3"
                                    ],
                                    "TransitGatewayId": "tgw-98765432109876543",
                                    "Tags": {
                                        "Name": "PRIVATE-EGRESS-VPC-TGW2",
                                        "Purpose": "Gateway Attach 2"
                                    },
                                    "RouteTables": {
                                        "InternalRT1": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ],
                                        "InternalRT2": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ],
                                        "InternalRT3": [
                                            {
                                                "RouteName": "Internal1",
                                                "RouteCIDR": "10.0.0.0/8"
                                            },
                                            {
                                                "RouteName": "Internal2",
                                                "RouteCIDR": "192.168.0.0/16"
                                            }
                                        ]
                                    }
                                }
                            },
                            "Tags": {
                                "Name": "PRIVATE-EGRESS-VPC",
                                "Template": "VPC for private endpoints egress only"
                            },
                            "NATGateways": {
                                "NATGW3": {
                                    "Subnet": "ReservedNet3",
                                    "Routetable": "InternalRT3"
                                },
                                "NATGW2": {
                                    "Subnet": "ReservedNet2",
                                    "Routetable": "InternalRT2"
                                },
                                "NATGW1": {
                                    "Subnet": "ReservedNet1",
                                    "Routetable": "InternalRT1"
                                }
                            },
                            "NetworkACLs": {
                                "InternalSubnetAcl": {
                                    "InternalSubnetAclEntryOutTCPUnreserved": "106,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNSIPv6": "113,17,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutUDPUnreserved": "107,6,allow,true,172.16.0.0/16,1024,65535",
                                    "InternalSubnetAclEntryOut": "100,-1,allow,true,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryOutSSH": "150,6,allow,true,0.0.0.0/0,22,22",
                                    "InternalSubnetAclEntryInUDPUnreservedIPv6": "105,17,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutTCPDNSIPv6": "112,6,allow,true,::/0,53,53",
                                    "InternalSubnetAclEntryOutTCPDNS": "110,6,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryOutHTTPS": "103,6,allow,true,0.0.0.0/0,443,443",
                                    "InternalSubnetAclEntryOutHTTP": "102,6,allow,true,0.0.0.0/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "InternalSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "InternalSubnetAclEntryInTCPUnreservedIPv6": "104,6,allow,false,::/0,1024,65535",
                                    "InternalSubnetAclEntryOutUDPDNS": "111,17,allow,true,0.0.0.0/0,53,53",
                                    "InternalSubnetAclEntryIn": "100,-1,allow,false,172.16.0.0/16,1,65535",
                                    "InternalSubnetAclEntryInTCPUnreserved": "102,6,allow,false,0.0.0.0/0,1024,65535",
                                    "InternalSubnetAclEntryInUDPUnreserved": "103,17,allow,false,0.0.0.0/0,1024,65535"
                                },
                                "RestrictedSubnetAcl": {
                                    "RestrictedSubnetAclEntryInUDPUnReserved": "91,17,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutSSH": "103,6,allow,true,0.0.0.0/0,22,22",
                                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": "151,6,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryOutHTTPSIPv6": "105,6,allow,true,::/0,443,443",
                                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": "92,6,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryNTP": "120,6,allow,true,0.0.0.0/0,123,123",
                                    "RestrictedSubnetAclEntryOutPuppet": "94,6,allow,true,172.16.0.0/16,8140,8140",
                                    "RestrictedSubnetAclEntryIn": "110,-1,allow,false,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTP": "101,6,allow,true,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPSIPv6": "104,6,allow,false,::/0,443,443",
                                    "RestrictedSubnetAclEntryInNetBios": "170,6,allow,false,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutDNSTCP": "150,6,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": "93,17,allow,false,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryInHTTP": "101,6,allow,false,0.0.0.0/0,80,80",
                                    "RestrictedSubnetAclEntryInHTTPIPv6": "103,6,allow,false,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutDNSUDP": "160,17,allow,true,0.0.0.0/0,53,53",
                                    "RestrictedSubnetAclEntryInTCPUnReserved": "90,6,allow,false,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutTCPUnReserved": "90,6,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInDNSTCP": "150,6,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": "93,17,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutNetBios1": "180,6,allow,true,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOut": "110,-1,allow,true,172.16.0.0/16,1,65535",
                                    "RestrictedSubnetAclEntryOutHTTPIPv6": "104,6,allow,true,::/0,80,80",
                                    "RestrictedSubnetAclEntryOutHTTPS": "102,6,allow,true,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryOutNetBios": "170,6,allow,true,172.16.0.0/16,389,389",
                                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": "92,6,allow,true,::/0,1024,65535",
                                    "RestrictedSubnetAclEntryOutUDPUnReserved": "91,17,allow,true,0.0.0.0/0,1024,65535",
                                    "RestrictedSubnetAclEntryInNetBios1": "80,6,allow,false,172.16.0.0/16,137,139",
                                    "RestrictedSubnetAclEntryOutSSHIPv6": "106,6,allow,true,::/0,22,22",
                                    "RestrictedSubnetAclEntryInHTTPS": "102,6,allow,false,0.0.0.0/0,443,443",
                                    "RestrictedSubnetAclEntryInDNSUDP": "160,17,allow,false,172.16.0.0/16,53,53",
                                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": "161,17,allow,true,::/0,53,53",
                                    "RestrictedSubnetAclEntryInSquid2": "140,6,allow,false,172.16.0.0/16,3128,3128"
                                }
                            },
                            "SecurityGroups": {
                                "VPCEndpoint": {
                                    "SecurityGroupIngress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ],
                                    "Tags": {
                                        "Name": "VPCEndpoint"
                                    },
                                    "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                                    "SecurityGroupEgress": [
                                        [
                                            "icmp",
                                            -1,
                                            -1,
                                            "172.16.0.0/20",
                                            "All ICMP Traffic"
                                        ],
                                        [
                                            "tcp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All TCP Traffic"
                                        ],
                                        [
                                            "udp",
                                            0,
                                            65535,
                                            "172.16.0.0/20",
                                            "All UDP Traffic"
                                        ]
                                    ]
                                }
                            },
                            "Details": {
                                "VPCDesc": "Private Egress VPC",
                                "Region": "ap-southeast-2",
                                "VPCName": "PRIVATEEGRESSVPC",
                                "IPv6": "true"
                            },
                            "DHCP": {
                                "NTPServers": "169.254.169.123",
                                "NTBType": 2,
                                "Name": "DhcpOptions",
                                "DNSServers": "172.16.0.2"
                            },
                            "CIDR": "172.16.0.0/20",
                            "Endpoints": {
                                "kinesis-streams": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudtrail": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "cloudformation": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "elasticloadbalancing": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ec2": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "logs": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "monitoring": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "s3": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "dynamodb": {
                                    "RouteTableIds": [
                                        "PublicRT",
                                        "InternalRT1",
                                        "InternalRT2",
                                        "InternalRT3"
                                    ],
                                    "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                                    "Type": "Gateway"
                                },
                                "ec2messages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "kms": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "config": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "events": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssm": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sns": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "sagemaker.runtime": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "codebuild": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "servicecatalog": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "execute-api": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "secretsmanager": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                },
                                "ssmmessages": {
                                    "SubnetIds": [
                                        "ReservedMgmt1",
                                        "ReservedMgmt2",
                                        "ReservedMgmt3"
                                    ],
                                    "Type": "Interface",
                                    "SecurityGroupIds": [
                                        "VPCEndpoint"
                                    ]
                                }
                            },
                            "RouteTables": {
                                "InternalRT3": "",
                                "PublicRT": [
                                    {
                                        "RouteName": "PublicRoute",
                                        "RouteCIDR": "0.0.0.0/0",
                                        "RouteGW": "InternetGateway"
                                    },
                                    {
                                        "RouteName": "PublicRouteIPv6",
                                        "RouteCIDR": "::/0",
                                        "RouteGW": "InternetGateway"
                                    }
                                ],
                                "InternalRT2": "",
                                "InternalRT1": ""
                            }
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "Mappings": {}
            },
            "region": "us-east-1",
            "params": {},
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "accountId": "012345678901"
        }
        test_assert = {
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064",
            "status": "success",
            "fragment": {
                "AWSTemplateFormatVersion": "2010-09-09",
                "Resources": {
                    "PRIVATEEGRESSVPC": {
                        "Type": "AWS::EC2::VPC",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/20",
                            "EnableDnsHostnames": True,
                            "EnableDnsSupport": True,
                            "InstanceTenancy": "default",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATEEGRESSVPC"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "IPv6Block": {
                        "Type": "AWS::EC2::VPCCidrBlock",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AmazonProvidedIpv6CidrBlock": True
                        }
                    },
                    "EgressGateway": {
                        "Type": "AWS::EC2::EgressOnlyInternetGateway",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "DhcpOptions": {
                        "Type": "AWS::EC2::DHCPOptions",
                        "Properties": {
                            "DomainNameServers": [
                                "172.16.0.2"
                            ],
                            "NtpServers": [
                                "169.254.169.123"
                            ],
                            "NetbiosNodeType": 2,
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "DhcpOptions"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "DhcpOptionsAssociation": {
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
                        "Properties": {
                            "DhcpOptionsId": {
                                "Ref": "DhcpOptions"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternetGateway": {
                        "Type": "AWS::EC2::InternetGateway",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternetGateway"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "IGWVPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "VPCFlowLogsRole": {
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
                    },
                    "VPCFlowLogs": {
                        "Type": "AWS::EC2::FlowLog",
                        "Properties": {
                            "DeliverLogsPermissionArn": {
                                "Fn::GetAtt": [
                                    "VPCFlowLogsRole",
                                    "Arn"
                                ]
                            },
                            "LogGroupName": "FlowLogsGroup",
                            "ResourceId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "ResourceType": "VPC",
                            "TrafficType": "ALL"
                        }
                    },
                    "Test1TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-01234567890123456",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Internal1"
                                },
                                {
                                    "Ref": "Internal2"
                                },
                                {
                                    "Ref": "Internal3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW1"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "Test2TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
                            "TransitGatewayId": "tgw-98765432109876543",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SubnetIds": [
                                {
                                    "Ref": "Internal1"
                                },
                                {
                                    "Ref": "Internal2"
                                },
                                {
                                    "Ref": "Internal3"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW2"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "Test2InternalRT1Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT1Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT2Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT2Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT3Internal1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "10.0.0.0/8",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "Test2InternalRT3Internal2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "192.168.0.0/16",
                            "TransitGatewayId": "tgw-98765432109876543",
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "DependsOn": [
                            "Test2TransitGWAttach"
                        ]
                    },
                    "InternalRT3": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "PublicRT": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PublicRT"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "PublicRoute": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "PublicRouteIPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "InternalRT2": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalRT1": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "ReservedMgmt1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.0/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        }
                    },
                    "ReservedMgmt3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        }
                    },
                    "Internal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.3.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    6,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        }
                    },
                    "Internal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        }
                    },
                    "Internal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.4.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    7,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        }
                    },
                    "Internal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        }
                    },
                    "Internal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.5.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    8,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        }
                    },
                    "Internal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        }
                    },
                    "ReservedNet3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    9,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    10,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.192/26",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    11,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        }
                    },
                    "ReservedNet1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        }
                    },
                    "PerimeterInternal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.6.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    3,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.7.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    4,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.8.0/24",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AssignIpv6AddressOnCreation": True,
                            "Ipv6CidrBlock": {
                                "Fn::Select": [
                                    5,
                                    {
                                        "Fn::Cidr": [
                                            {
                                                "Fn::Select": [
                                                    0,
                                                    {
                                                        "Fn::GetAtt": [
                                                            "PRIVATEEGRESSVPC",
                                                            "Ipv6CidrBlocks"
                                                        ]
                                                    }
                                                ]
                                            },
                                            12,
                                            64
                                        ]
                                    }
                                ]
                            }
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        }
                    },
                    "PerimeterInternal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 113
                        }
                    },
                    "InternalSubnetAclEntryOutUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 107
                        }
                    },
                    "InternalSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 112
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "InternalSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 111
                        }
                    },
                    "InternalSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 100
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "RestrictedSubnetAcl"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 151
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 105
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryNTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 123,
                                "To": 123
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 120
                        }
                    },
                    "RestrictedSubnetAclEntryOutPuppet": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 8140,
                                "To": 8140
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 94
                        }
                    },
                    "RestrictedSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 101
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 103
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 90
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 150
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 93
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 180
                        }
                    },
                    "RestrictedSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1,
                                "To": 65535
                            },
                            "Protocol": -1,
                            "RuleAction": "allow",
                            "RuleNumber": 110
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 80,
                                "To": 80
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 104
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 389,
                                "To": 389
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 170
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 92
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 1024,
                                "To": 65535
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 91
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 137,
                                "To": 139
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 80
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSHIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 22,
                                "To": 22
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 106
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "0.0.0.0/0",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 443,
                                "To": 443
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 102
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 160
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "Ipv6CidrBlock": "::/0",
                            "Egress": True,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 53,
                                "To": 53
                            },
                            "Protocol": 17,
                            "RuleAction": "allow",
                            "RuleNumber": 161
                        }
                    },
                    "RestrictedSubnetAclEntryInSquid2": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "CidrBlock": "172.16.0.0/16",
                            "Egress": False,
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "PortRange": {
                                "From": 3128,
                                "To": 3128
                            },
                            "Protocol": 6,
                            "RuleAction": "allow",
                            "RuleNumber": 140
                        }
                    },
                    "EIPNATGW3": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW3": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW3",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW3"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT3NATGW3": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "InternalRT3NATGW3IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW2": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW2",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW2"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT2NATGW2": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "InternalRT2NATGW2IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "NATGW1": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW1",
                                    "AllocationId"
                                ]
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            },
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "NATGW1"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "InternalRT1NATGW1": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "InternalRT1NATGW1IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "VPCEndpoint": {
                        "Type": "AWS::EC2::SecurityGroup",
                        "Properties": {
                            "GroupName": "VPCEndpoint",
                            "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "SecurityGroupIngress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "SecurityGroupEgress": [
                                {
                                    "IpProtocol": "icmp",
                                    "FromPort": -1,
                                    "ToPort": -1,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic"
                                },
                                {
                                    "IpProtocol": "tcp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic"
                                },
                                {
                                    "IpProtocol": "udp",
                                    "FromPort": 0,
                                    "ToPort": 65535,
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic"
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "VPCEndpoint"
                                },
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC"
                                },
                                {
                                    "Key": "Template",
                                    "Value": "VPC for private endpoints egress only"
                                }
                            ]
                        }
                    },
                    "kinesisstreamsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kinesis-streams"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudtrailEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudtrail"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "cloudformationEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".cloudformation"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "elasticloadbalancingEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".elasticloadbalancing"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ec2EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "logsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".logs"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "monitoringEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".monitoring"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "s3EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".s3"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "InternalRT1"
                                },
                                {
                                    "Ref": "InternalRT2"
                                },
                                {
                                    "Ref": "InternalRT3"
                                }
                            ]
                        }
                    },
                    "dynamodbEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".dynamodb"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Gateway",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
                            "RouteTableIds": [
                                {
                                    "Ref": "PublicRT"
                                },
                                {
                                    "Ref": "InternalRT1"
                                },
                                {
                                    "Ref": "InternalRT2"
                                },
                                {
                                    "Ref": "InternalRT3"
                                }
                            ]
                        }
                    },
                    "ec2messagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ec2messages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "kmsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".kms"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "configEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".config"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "eventsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".events"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssm"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "snsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sns"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "sagemakerruntimeEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".sagemaker.runtime"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "codebuildEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".codebuild"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "servicecatalogEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".servicecatalog"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "executeapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".execute-api"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "secretsmanagerEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".secretsmanager"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    },
                    "ssmmessagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "ServiceName": {
                                "Fn::Join": [
                                    "",
                                    [
                                        "com.amazonaws.",
                                        {
                                            "Ref": "AWS::Region"
                                        },
                                        ".ssmmessages"
                                    ]
                                ]
                            },
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "PrivateDnsEnabled": True,
                            "SubnetIds": [
                                {
                                    "Ref": "ReservedMgmt1"
                                },
                                {
                                    "Ref": "ReservedMgmt2"
                                },
                                {
                                    "Ref": "ReservedMgmt3"
                                }
                            ],
                            "SecurityGroupIds": [
                                {
                                    "Ref": "VPCEndpoint"
                                }
                            ]
                        }
                    }
                },
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "Mappings": {},
                "Outputs": {
                    "PRIVATEEGRESSVPC": {
                        "Description": "PRIVATEEGRESSVPC",
                        "Value": {
                            "Ref": "PRIVATEEGRESSVPC"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-VPCid"
                            }
                        }
                    },
                    "InternalRT3": {
                        "Description": "InternalRT3",
                        "Value": {
                            "Ref": "InternalRT3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT3"
                            }
                        }
                    },
                    "PublicRT": {
                        "Description": "PublicRT",
                        "Value": {
                            "Ref": "PublicRT"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PublicRT"
                            }
                        }
                    },
                    "InternalRT2": {
                        "Description": "InternalRT2",
                        "Value": {
                            "Ref": "InternalRT2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT2"
                            }
                        }
                    },
                    "InternalRT1": {
                        "Description": "InternalRT1",
                        "Value": {
                            "Ref": "InternalRT1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT1"
                            }
                        }
                    },
                    "ReservedMgmt1": {
                        "Description": "ReservedMgmt1",
                        "Value": {
                            "Ref": "ReservedMgmt1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt1"
                            }
                        }
                    },
                    "ReservedMgmt2": {
                        "Description": "ReservedMgmt2",
                        "Value": {
                            "Ref": "ReservedMgmt2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt2"
                            }
                        }
                    },
                    "ReservedMgmt3": {
                        "Description": "ReservedMgmt3",
                        "Value": {
                            "Ref": "ReservedMgmt3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt3"
                            }
                        }
                    },
                    "Internal1": {
                        "Description": "Internal1",
                        "Value": {
                            "Ref": "Internal1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal1"
                            }
                        }
                    },
                    "Internal2": {
                        "Description": "Internal2",
                        "Value": {
                            "Ref": "Internal2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal2"
                            }
                        }
                    },
                    "Internal3": {
                        "Description": "Internal3",
                        "Value": {
                            "Ref": "Internal3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal3"
                            }
                        }
                    },
                    "ReservedNet3": {
                        "Description": "ReservedNet3",
                        "Value": {
                            "Ref": "ReservedNet3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet3"
                            }
                        }
                    },
                    "ReservedNet2": {
                        "Description": "ReservedNet2",
                        "Value": {
                            "Ref": "ReservedNet2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet2"
                            }
                        }
                    },
                    "ReservedNet1": {
                        "Description": "ReservedNet1",
                        "Value": {
                            "Ref": "ReservedNet1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet1"
                            }
                        }
                    },
                    "PerimeterInternal1": {
                        "Description": "PerimeterInternal1",
                        "Value": {
                            "Ref": "PerimeterInternal1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal1"
                            }
                        }
                    },
                    "PerimeterInternal2": {
                        "Description": "PerimeterInternal2",
                        "Value": {
                            "Ref": "PerimeterInternal2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal2"
                            }
                        }
                    },
                    "PerimeterInternal3": {
                        "Description": "PerimeterInternal3",
                        "Value": {
                            "Ref": "PerimeterInternal3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal3"
                            }
                        }
                    },
                    "InternalSubnetAcl": {
                        "Description": "InternalSubnetAcl",
                        "Value": {
                            "Ref": "InternalSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-InternalSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Description": "RestrictedSubnetAcl",
                        "Value": {
                            "Ref": "RestrictedSubnetAcl"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-RestrictedSubnetAcl"
                            }
                        }
                    },
                    "EIPNATGW3": {
                        "Description": "EIP for NATGW3",
                        "Value": {
                            "Ref": "EIPNATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW3"
                            }
                        }
                    },
                    "NATGW3": {
                        "Description": "NATGW3",
                        "Value": {
                            "Ref": "NATGW3"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW3"
                            }
                        }
                    },
                    "EIPNATGW2": {
                        "Description": "EIP for NATGW2",
                        "Value": {
                            "Ref": "EIPNATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW2"
                            }
                        }
                    },
                    "NATGW2": {
                        "Description": "NATGW2",
                        "Value": {
                            "Ref": "NATGW2"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW2"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Description": "EIP for NATGW1",
                        "Value": {
                            "Ref": "EIPNATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW1"
                            }
                        }
                    },
                    "NATGW1": {
                        "Description": "NATGW1",
                        "Value": {
                            "Ref": "NATGW1"
                        },
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW1"
                            }
                        }
                    }
                }
            }
        }
        actual = src.macro.handler(transform_call, "")
        print("#####\n\n")
        print(json.dumps(actual))
        print("#####\n\n")
        self.assertEquals(test_assert, actual)
