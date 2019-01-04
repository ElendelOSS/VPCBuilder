import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderCoreLogicSetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = None


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
                    "KABLAMOBUILDVPC": {
                        "Type": "Kablamo::Network::VPC",
                        "Properties": {
                            "Subnets": {
                                "ReservedMgmt1": {
                                    "CIDR": "172.16.0.0/26",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "ReservedMgmt2": {
                                    "CIDR": "172.16.1.0/26",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "ReservedMgmt3": {
                                    "CIDR": "172.16.2.0/26",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
                                },
                                "Internal1": {
                                    "CIDR": "172.16.3.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "Internal2": {
                                    "CIDR": "172.16.4.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "Internal3": {
                                    "CIDR": "172.16.5.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
                                },
                                "ReservedNet3": {
                                    "CIDR": "172.16.2.192/26",
                                    "AZ": 2,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "ReservedNet2": {
                                    "CIDR": "172.16.1.192/26",
                                    "AZ": 1,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "ReservedNet1": {
                                    "CIDR": "172.16.0.192/26",
                                    "AZ": 0,
                                    "NetACL": "RestrictedSubnetAcl",
                                    "RouteTable": "PublicRT"
                                },
                                "PerimeterInternal1": {
                                    "CIDR": "172.16.6.0/24",
                                    "AZ": 0,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT1"
                                },
                                "PerimeterInternal2": {
                                    "CIDR": "172.16.7.0/24",
                                    "AZ": 1,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT2"
                                },
                                "PerimeterInternal3": {
                                    "CIDR": "172.16.8.0/24",
                                    "AZ": 2,
                                    "NetACL": "InternalSubnetAcl",
                                    "RouteTable": "InternalRT3"
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
            "status": "success",
            "fragment": {
                "Description": "Private VPC Template",
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Type": "String",
                        "Description": "VPC Gateway"
                    }
                },
                "AWSTemplateFormatVersion": "2010-09-09",
                "Outputs": {
                    "NATGW3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW3"
                            }
                        },
                        "Description": "NATGW3",
                        "Value": {
                            "Ref": "NATGW3"
                        }
                    },
                    "NATGW2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW2"
                            }
                        },
                        "Description": "NATGW2",
                        "Value": {
                            "Ref": "NATGW2"
                        }
                    },
                    "NATGW1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW1"
                            }
                        },
                        "Description": "NATGW1",
                        "Value": {
                            "Ref": "NATGW1"
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-RestrictedSubnetAcl"
                            }
                        },
                        "Description": "RestrictedSubnetAcl",
                        "Value": {
                            "Ref": "RestrictedSubnetAcl"
                        }
                    },
                    "PRIVATEEGRESSVPC": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-VPCid"
                            }
                        },
                        "Description": "PRIVATEEGRESSVPC",
                        "Value": {
                            "Ref": "PRIVATEEGRESSVPC"
                        }
                    },
                    "EIPNATGW2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW2"
                            }
                        },
                        "Description": "EIP for NATGW2",
                        "Value": {
                            "Ref": "EIPNATGW2"
                        }
                    },
                    "ReservedNet2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet2"
                            }
                        },
                        "Description": "ReservedNet2",
                        "Value": {
                            "Ref": "ReservedNet2"
                        }
                    },
                    "Internal1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal1"
                            }
                        },
                        "Description": "Internal1",
                        "Value": {
                            "Ref": "Internal1"
                        }
                    },
                    "Internal2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal2"
                            }
                        },
                        "Description": "Internal2",
                        "Value": {
                            "Ref": "Internal2"
                        }
                    },
                    "Internal3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal3"
                            }
                        },
                        "Description": "Internal3",
                        "Value": {
                            "Ref": "Internal3"
                        }
                    },
                    "ReservedNet3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet3"
                            }
                        },
                        "Description": "ReservedNet3",
                        "Value": {
                            "Ref": "ReservedNet3"
                        }
                    },
                    "EIPNATGW3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW3"
                            }
                        },
                        "Description": "EIP for NATGW3",
                        "Value": {
                            "Ref": "EIPNATGW3"
                        }
                    },
                    "ReservedNet1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet1"
                            }
                        },
                        "Description": "ReservedNet1",
                        "Value": {
                            "Ref": "ReservedNet1"
                        }
                    },
                    "EIPNATGW1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW1"
                            }
                        },
                        "Description": "EIP for NATGW1",
                        "Value": {
                            "Ref": "EIPNATGW1"
                        }
                    },
                    "ReservedMgmt1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt1"
                            }
                        },
                        "Description": "ReservedMgmt1",
                        "Value": {
                            "Ref": "ReservedMgmt1"
                        }
                    },
                    "ReservedMgmt2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt2"
                            }
                        },
                        "Description": "ReservedMgmt2",
                        "Value": {
                            "Ref": "ReservedMgmt2"
                        }
                    },
                    "ReservedMgmt3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt3"
                            }
                        },
                        "Description": "ReservedMgmt3",
                        "Value": {
                            "Ref": "ReservedMgmt3"
                        }
                    },
                    "PublicRT": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PublicRT"
                            }
                        },
                        "Description": "PublicRT",
                        "Value": {
                            "Ref": "PublicRT"
                        }
                    },
                    "PerimeterInternal1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal1"
                            }
                        },
                        "Description": "PerimeterInternal1",
                        "Value": {
                            "Ref": "PerimeterInternal1"
                        }
                    },
                    "PerimeterInternal2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal2"
                            }
                        },
                        "Description": "PerimeterInternal2",
                        "Value": {
                            "Ref": "PerimeterInternal2"
                        }
                    },
                    "PerimeterInternal3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal3"
                            }
                        },
                        "Description": "PerimeterInternal3",
                        "Value": {
                            "Ref": "PerimeterInternal3"
                        }
                    },
                    "InternalRT1": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT1"
                            }
                        },
                        "Description": "InternalRT1",
                        "Value": {
                            "Ref": "InternalRT1"
                        }
                    },
                    "InternalRT2": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT2"
                            }
                        },
                        "Description": "InternalRT2",
                        "Value": {
                            "Ref": "InternalRT2"
                        }
                    },
                    "InternalRT3": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT3"
                            }
                        },
                        "Description": "InternalRT3",
                        "Value": {
                            "Ref": "InternalRT3"
                        }
                    },
                    "InternalSubnetAcl": {
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-InternalSubnetAcl"
                            }
                        },
                        "Description": "InternalSubnetAcl",
                        "Value": {
                            "Ref": "InternalSubnetAcl"
                        }
                    }
                },
                "Resources": {
                    "RestrictedSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "105",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            }
                        }
                    },
                    "PerimeterInternal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "Internal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal2"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInSquid2": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "140",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "3128",
                                "From": "3128"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "113",
                            "Protocol": "17",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            }
                        }
                    },
                    "VPCFlowLogsRole": {
                        "Type": "AWS::IAM::Role",
                        "Properties": {
                            "Path": "/",
                            "Policies": [
                                {
                                    "PolicyName": "root",
                                    "PolicyDocument": {
                                        "Version": "2012-10-17",
                                        "Statement": [
                                            {
                                                "Action": [
                                                    "logs:*"
                                                ],
                                                "Resource": "arn:aws:logs:*:*:*",
                                                "Effect": "Allow"
                                            }
                                        ]
                                    }
                                }
                            ],
                            "AssumeRolePolicyDocument": {
                                "Version": "2012-10-17",
                                "Statement": [
                                    {
                                        "Action": [
                                            "sts:AssumeRole"
                                        ],
                                        "Effect": "Allow",
                                        "Principal": {
                                            "Service": [
                                                "vpc-flow-logs.amazonaws.com"
                                            ]
                                        }
                                    }
                                ]
                            }
                        }
                    },
                    "Internal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal3"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "103",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "ReservedNet3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            },
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            }
                        }
                    },
                    "s3EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
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
                            ],
                            "VpcEndpointType": "Gateway",
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
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
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "Test1TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
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
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "TransitGatewayId": "tgw-01234567890123456",
                            "Tags": [
                                {
                                    "Value": "PRIVATE-EGRESS-VPC-TGW1",
                                    "Key": "Name"
                                },
                                {
                                    "Value": "Gateway Attach 1",
                                    "Key": "Purpose"
                                }
                            ]
                        }
                    },
                    "dynamodbEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
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
                            ],
                            "VpcEndpointType": "Gateway",
                            "PolicyDocument": "{\n    \"Version\":\"2012-10-17\",\n    \"Statement\":[\n        {\n            \"Effect\":\"Allow\",\n            \"Principal\": \"*\",\n            \"Action\":[\"s3:*\"],\n            \"Resource\":[\"*\"]\n        }\n    ]\n}\n",
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
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "Internal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "Internal1",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.3.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "Internal2",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.4.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Internal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "Internal3",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.5.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "InternalSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "103",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "150",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "ReservedNet3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedNet3",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.192/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedNet2",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.192/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedNet1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedNet1",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.192/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "RouteNATGW1IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "DestinationIpv6CidrBlock": "::/0",
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "ec2EndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "101",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "InternalSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "102",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "ReservedMgmt1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "ReservedNet2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "103",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "22",
                                "From": "22"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "Internal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal1"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "cloudtrailEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "93",
                            "Protocol": "17",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
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
                    "ReservedMgmt2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "kmsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "ReservedMgmt3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "PublicRouteIPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "DestinationIpv6CidrBlock": "::/0"
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "80",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "139",
                                "From": "137"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "160",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryInUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "91",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
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
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "RouteTableId": {
                                "Ref": "PublicRT"
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
                    "RestrictedSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "110",
                            "Protocol": "-1",
                            "PortRange": {
                                "To": "65535",
                                "From": "1"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "RouteNATGW3IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "DestinationIpv6CidrBlock": "::/0",
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "105",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            }
                        }
                    },
                    "InternalSubnetAclEntryIn": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "100",
                            "Protocol": "-1",
                            "PortRange": {
                                "To": "65535",
                                "From": "1"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "logsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "IPv6Block": {
                        "Type": "AWS::EC2::VPCCidrBlock",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "AmazonProvidedIpv6CidrBlock": "true"
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "104",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            }
                        }
                    },
                    "InternalSubnetAclEntryInUDPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "105",
                            "Protocol": "17",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "170",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "389",
                                "From": "389"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "PerimeterInternal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutSSHIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "106",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "22",
                                "From": "22"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "93",
                            "Protocol": "17",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "110",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "RestrictedSubnetAcl",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "ReservedNet3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "InternalSubnetAclEntryOutSSH": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "150",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "22",
                                "From": "22"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "PublicRT": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "PublicRT",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "PRIVATEEGRESSVPC": {
                        "Type": "AWS::EC2::VPC",
                        "Properties": {
                            "InstanceTenancy": "default",
                            "EnableDnsSupport": 'true',
                            "CidrBlock": "172.16.0.0/20",
                            "EnableDnsHostnames": 'true',
                            "Tags": [
                                {
                                    "Value": "PRIVATEEGRESSVPC",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "102",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryOutPuppet": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "94",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "8140",
                                "From": "8140"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "PerimeterInternal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "executeapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "ReservedMgmt3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "InternalRT1": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "InternalRT1",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "InternalRT2": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "InternalRT2",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "InternalRT3": {
                        "Type": "AWS::EC2::RouteTable",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "InternalRT3",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "elasticloadbalancingEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "IGWVPCGatewayAttachment": {
                        "Type": "AWS::EC2::VPCGatewayAttachment",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            }
                        }
                    },
                    "Internal1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "102",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "InternalSubnetAclEntryOutUDPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "107",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSUDP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "160",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "InternalSubnetAclEntryOutTCPUnreserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "106",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "151",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            }
                        }
                    },
                    "servicecatalogEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "ssmEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "Internal2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "InternetGateway": {
                        "Type": "AWS::EC2::InternetGateway",
                        "Properties": {
                            "Tags": [
                                {
                                    "Value": "InternetGateway",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "RestrictedSubnetAclEntryNTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "120",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "123",
                                "From": "123"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RouteNATGW1": {
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
                    "EgressGateway": {
                        "Type": "AWS::EC2::EgressOnlyInternetGateway",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        }
                    },
                    "RouteNATGW3": {
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
                    "RouteNATGW2": {
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
                    "InternalSubnetAcl": {
                        "Type": "AWS::EC2::NetworkAcl",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "InternalSubnetAcl",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "ssmmessagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "codebuildEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "InternalSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "100",
                            "Protocol": "-1",
                            "PortRange": {
                                "To": "65535",
                                "From": "1"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "NATGW1": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            },
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW1",
                                    "AllocationId"
                                ]
                            },
                            "Tags": [
                                {
                                    "Value": "NATGW1",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "ReservedNet1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        }
                    },
                    "ReservedMgmt1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedMgmt1",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.0/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedMgmt2",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.0/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "ReservedMgmt3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "ReservedMgmt3",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.0/26",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "RouteNATGW2IPv6": {
                        "Type": "AWS::EC2::Route",
                        "Properties": {
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "DestinationIpv6CidrBlock": "::/0",
                            "RouteTableId": {
                                "Ref": "InternalRT2"
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
                    "PerimeterInternal1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "ReservedNet2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            },
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOut": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "110",
                            "Protocol": "-1",
                            "PortRange": {
                                "To": "65535",
                                "From": "1"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "PerimeterInternal2SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "104",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTPS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "102",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "443",
                                "From": "443"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "ec2messagesEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "92",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            }
                        }
                    },
                    "eventsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "monitoringEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "VPCEndpoint": {
                        "Type": "AWS::EC2::SecurityGroup",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "VPCEndpoint",
                                    "Key": "Name"
                                }
                            ],
                            "SecurityGroupEgress": [
                                {
                                    "ToPort": -1,
                                    "IpProtocol": "icmp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic",
                                    "FromPort": -1
                                },
                                {
                                    "ToPort": 65535,
                                    "IpProtocol": "tcp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic",
                                    "FromPort": 0
                                },
                                {
                                    "ToPort": 65535,
                                    "IpProtocol": "udp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic",
                                    "FromPort": 0
                                }
                            ],
                            "SecurityGroupIngress": [
                                {
                                    "ToPort": -1,
                                    "IpProtocol": "icmp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic",
                                    "FromPort": -1
                                },
                                {
                                    "ToPort": 65535,
                                    "IpProtocol": "tcp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic",
                                    "FromPort": 0
                                },
                                {
                                    "ToPort": 65535,
                                    "IpProtocol": "udp",
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic",
                                    "FromPort": 0
                                }
                            ],
                            "GroupName": "VPCEndpoint",
                            "GroupDescription": "VPC Endpoint Interface Firewall Rules"
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
                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "92",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            }
                        }
                    },
                    "snsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "sagemakerapiEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "ReservedMgmt1SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        }
                    },
                    "kinesisstreamsEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "RestrictedSubnetAclEntryInTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "90",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "VPCFlowLogs": {
                        "Type": "AWS::EC2::FlowLog",
                        "Properties": {
                            "ResourceType": "VPC",
                            "ResourceId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "DeliverLogsPermissionArn": {
                                "Fn::GetAtt": [
                                    "VPCFlowLogsRole",
                                    "Arn"
                                ]
                            },
                            "LogGroupName": "FlowLogsGroup",
                            "TrafficType": "ALL"
                        }
                    },
                    "NATGW3": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            },
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW3",
                                    "AllocationId"
                                ]
                            },
                            "Tags": [
                                {
                                    "Value": "NATGW3",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "NATGW2": {
                        "Type": "AWS::EC2::NatGateway",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            },
                            "AllocationId": {
                                "Fn::GetAtt": [
                                    "EIPNATGW2",
                                    "AllocationId"
                                ]
                            },
                            "Tags": [
                                {
                                    "Value": "NATGW2",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "DhcpOptions": {
                        "Type": "AWS::EC2::DHCPOptions",
                        "Properties": {
                            "NtpServers": [
                                "169.254.169.123"
                            ],
                            "NetbiosNodeType": 2,
                            "DomainNameServers": [
                                "172.16.0.2"
                            ],
                            "Tags": [
                                {
                                    "Value": "DhcpOptions",
                                    "Key": "Name"
                                }
                            ]
                        }
                    },
                    "secretsmanagerEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "ReservedNet1SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            },
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            }
                        }
                    },
                    "Internal3SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "Internal3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        }
                    },
                    "sagemakerruntimeEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "InternalSubnetAclEntryOutUDPDNS": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "111",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryOutHTTP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "101",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "InternalSubnetAclEntryOutTCPDNSIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "112",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            }
                        }
                    },
                    "configEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    },
                    "EIPNATGW2": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "EIPNATGW3": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "InternalSubnetAclEntryOutHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "104",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            }
                        }
                    },
                    "EIPNATGW1": {
                        "Type": "AWS::EC2::EIP",
                        "Properties": {
                            "Domain": "vpc"
                        }
                    },
                    "PerimeterInternal3SubnetNetworkACLAssociation": {
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            },
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryInHTTPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "103",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "80",
                                "From": "80"
                            }
                        }
                    },
                    "ReservedMgmt2SubnetRoutetableAssociation": {
                        "Type": "AWS::EC2::SubnetRouteTableAssociation",
                        "Properties": {
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "90",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryInDNSTCP": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "150",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            },
                            "Egress": "false",
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "DhcpOptionsAssociation": {
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "DhcpOptionsId": {
                                "Ref": "DhcpOptions"
                            }
                        }
                    },
                    "PerimeterInternal1": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "PerimeterInternal1",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.6.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal2": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "PerimeterInternal2",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.7.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "PerimeterInternal3": {
                        "Type": "AWS::EC2::Subnet",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "Tags": [
                                {
                                    "Value": "PerimeterInternal3",
                                    "Key": "Name"
                                }
                            ],
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
                            },
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.8.0/24",
                            "AssignIpv6AddressOnCreation": True
                        },
                        "DependsOn": "IPv6Block"
                    },
                    "Test2TransitGWAttach": {
                        "Type": "AWS::EC2::TransitGatewayAttachment",
                        "Properties": {
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
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "TransitGatewayId": "tgw-98765432109876543",
                            "Tags": [
                                {
                                    "Value": "PRIVATE-EGRESS-VPC-TGW2",
                                    "Key": "Name"
                                },
                                {
                                    "Value": "Gateway Attach 2",
                                    "Key": "Purpose"
                                }
                            ]
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "170",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "389",
                                "From": "389"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "InternalSubnetAclEntryInTCPUnreservedIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "RuleNumber": "104",
                            "Protocol": "6",
                            "Ipv6CidrBlock": "::/0",
                            "Egress": "false",
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            }
                        }
                    },
                    "RestrictedSubnetAclEntryOutNetBios1": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "180",
                            "Protocol": "6",
                            "PortRange": {
                                "To": "139",
                                "From": "137"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "172.16.0.0/16"
                        }
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReserved": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "91",
                            "Protocol": "17",
                            "PortRange": {
                                "To": "65535",
                                "From": "1024"
                            },
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "CidrBlock": "0.0.0.0/0"
                        }
                    },
                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": {
                        "Type": "AWS::EC2::NetworkAclEntry",
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "RuleNumber": "161",
                            "Protocol": "17",
                            "Ipv6CidrBlock": "::/0",
                            'Egress': 'true',
                            "RuleAction": "allow",
                            "PortRange": {
                                "To": "53",
                                "From": "53"
                            }
                        }
                    },
                    "cloudformationEndPoint": {
                        "Type": "AWS::EC2::VPCEndpoint",
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
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
                            ],
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
                            "PrivateDnsEnabled": True,
                            "VpcEndpointType": "Interface"
                        }
                    }
                },
                "Mappings": {}
            },
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064"
        }
        actual = src.macro.handler(transform_call, "")
        self.assertEquals(test_assert, actual)
