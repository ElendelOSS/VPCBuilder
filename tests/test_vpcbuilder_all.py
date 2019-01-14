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
                        "Type": "Elendel::Network::VPC",
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
                "AWSTemplateFormatVersion": "2010-09-09",
                "Description": "Private VPC Template",
                "Mappings": {},
                "Outputs": {
                    "EIPNATGW1": {
                        "Description": "EIP for NATGW1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW1"
                            }
                        },
                        "Value": {
                            "Ref": "EIPNATGW1"
                        }
                    },
                    "EIPNATGW2": {
                        "Description": "EIP for NATGW2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW2"
                            }
                        },
                        "Value": {
                            "Ref": "EIPNATGW2"
                        }
                    },
                    "EIPNATGW3": {
                        "Description": "EIP for NATGW3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-EIP-NATGW3"
                            }
                        },
                        "Value": {
                            "Ref": "EIPNATGW3"
                        }
                    },
                    "Internal1": {
                        "Description": "Internal1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal1"
                            }
                        },
                        "Value": {
                            "Ref": "Internal1"
                        }
                    },
                    "Internal2": {
                        "Description": "Internal2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal2"
                            }
                        },
                        "Value": {
                            "Ref": "Internal2"
                        }
                    },
                    "Internal3": {
                        "Description": "Internal3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-Internal3"
                            }
                        },
                        "Value": {
                            "Ref": "Internal3"
                        }
                    },
                    "InternalRT1": {
                        "Description": "InternalRT1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT1"
                            }
                        },
                        "Value": {
                            "Ref": "InternalRT1"
                        }
                    },
                    "InternalRT2": {
                        "Description": "InternalRT2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT2"
                            }
                        },
                        "Value": {
                            "Ref": "InternalRT2"
                        }
                    },
                    "InternalRT3": {
                        "Description": "InternalRT3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-InternalRT3"
                            }
                        },
                        "Value": {
                            "Ref": "InternalRT3"
                        }
                    },
                    "InternalSubnetAcl": {
                        "Description": "InternalSubnetAcl",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-InternalSubnetAcl"
                            }
                        },
                        "Value": {
                            "Ref": "InternalSubnetAcl"
                        }
                    },
                    "NATGW1": {
                        "Description": "NATGW1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW1"
                            }
                        },
                        "Value": {
                            "Ref": "NATGW1"
                        }
                    },
                    "NATGW2": {
                        "Description": "NATGW2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW2"
                            }
                        },
                        "Value": {
                            "Ref": "NATGW2"
                        }
                    },
                    "NATGW3": {
                        "Description": "NATGW3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NATGW-NATGW3"
                            }
                        },
                        "Value": {
                            "Ref": "NATGW3"
                        }
                    },
                    "PRIVATEEGRESSVPC": {
                        "Description": "PRIVATEEGRESSVPC",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-VPCid"
                            }
                        },
                        "Value": {
                            "Ref": "PRIVATEEGRESSVPC"
                        }
                    },
                    "PerimeterInternal1": {
                        "Description": "PerimeterInternal1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal1"
                            }
                        },
                        "Value": {
                            "Ref": "PerimeterInternal1"
                        }
                    },
                    "PerimeterInternal2": {
                        "Description": "PerimeterInternal2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal2"
                            }
                        },
                        "Value": {
                            "Ref": "PerimeterInternal2"
                        }
                    },
                    "PerimeterInternal3": {
                        "Description": "PerimeterInternal3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-PerimeterInternal3"
                            }
                        },
                        "Value": {
                            "Ref": "PerimeterInternal3"
                        }
                    },
                    "PublicRT": {
                        "Description": "PublicRT",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-RouteTable-PublicRT"
                            }
                        },
                        "Value": {
                            "Ref": "PublicRT"
                        }
                    },
                    "ReservedMgmt1": {
                        "Description": "ReservedMgmt1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt1"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedMgmt1"
                        }
                    },
                    "ReservedMgmt2": {
                        "Description": "ReservedMgmt2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt2"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedMgmt2"
                        }
                    },
                    "ReservedMgmt3": {
                        "Description": "ReservedMgmt3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedMgmt3"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedMgmt3"
                        }
                    },
                    "ReservedNet1": {
                        "Description": "ReservedNet1",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet1"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedNet1"
                        }
                    },
                    "ReservedNet2": {
                        "Description": "ReservedNet2",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet2"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedNet2"
                        }
                    },
                    "ReservedNet3": {
                        "Description": "ReservedNet3",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-Subnet-ReservedNet3"
                            }
                        },
                        "Value": {
                            "Ref": "ReservedNet3"
                        }
                    },
                    "RestrictedSubnetAcl": {
                        "Description": "RestrictedSubnetAcl",
                        "Export": {
                            "Name": {
                                "Fn::Sub": "${AWS::StackName}-NACL-RestrictedSubnetAcl"
                            }
                        },
                        "Value": {
                            "Ref": "RestrictedSubnetAcl"
                        }
                    }
                },
                "Parameters": {
                    "VGW": {
                        "Default": "vgw-012345678",
                        "Description": "VPC Gateway",
                        "Type": "String"
                    }
                },
                "Resources": {
                    "DhcpOptions": {
                        "Properties": {
                            "DomainNameServers": [
                                "172.16.0.2"
                            ],
                            "NetbiosNodeType": 2,
                            "NtpServers": [
                                "169.254.169.123"
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "DhcpOptions"
                                }
                            ]
                        },
                        "Type": "AWS::EC2::DHCPOptions"
                    },
                    "DhcpOptionsAssociation": {
                        "Properties": {
                            "DhcpOptionsId": {
                                "Ref": "DhcpOptions"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCDHCPOptionsAssociation"
                    },
                    "EIPNATGW1": {
                        "Properties": {
                            "Domain": "vpc"
                        },
                        "Type": "AWS::EC2::EIP"
                    },
                    "EIPNATGW2": {
                        "Properties": {
                            "Domain": "vpc"
                        },
                        "Type": "AWS::EC2::EIP"
                    },
                    "EIPNATGW3": {
                        "Properties": {
                            "Domain": "vpc"
                        },
                        "Type": "AWS::EC2::EIP"
                    },
                    "EgressGateway": {
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::EgressOnlyInternetGateway"
                    },
                    "IGWVPCGatewayAttachment": {
                        "Properties": {
                            "InternetGatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCGatewayAttachment"
                    },
                    "IPv6Block": {
                        "Properties": {
                            "AmazonProvidedIpv6CidrBlock": True,
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCCidrBlock"
                    },
                    "Internal1": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.3.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal1"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "Internal1SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "Internal1SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "Internal1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "Internal2": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.4.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal2"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "Internal2SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "Internal2SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "Internal2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "Internal3": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.5.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "Internal3"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "Internal3SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "Internal3SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "Internal3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "InternalRT1": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT1"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::RouteTable"
                    },
                    "InternalRT1RoutePropagation": {
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ],
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
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation"
                    },
                    "InternalRT2": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT2"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::RouteTable"
                    },
                    "InternalRT2RoutePropagation": {
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ],
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
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation"
                    },
                    "InternalRT3": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalRT3"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::RouteTable"
                    },
                    "InternalRT3RoutePropagation": {
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ],
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
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation"
                    },
                    "InternalSubnetAcl": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternalSubnetAcl"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::NetworkAcl"
                    },
                    "InternalSubnetAclEntryIn": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryInTCPUnreserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryInTCPUnreservedIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryInUDPUnreserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryInUDPUnreservedIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOut": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutHTTP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutHTTPIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutHTTPS": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutHTTPSIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutSSH": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutTCPDNS": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutTCPDNSIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutTCPUnreserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutUDPDNS": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutUDPDNSIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternalSubnetAclEntryOutUDPUnreserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "InternetGateway": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "InternetGateway"
                                }
                            ]
                        },
                        "Type": "AWS::EC2::InternetGateway"
                    },
                    "NATGW1": {
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
                                }
                            ]
                        },
                        "Type": "AWS::EC2::NatGateway"
                    },
                    "NATGW2": {
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
                                }
                            ]
                        },
                        "Type": "AWS::EC2::NatGateway"
                    },
                    "NATGW3": {
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
                                }
                            ]
                        },
                        "Type": "AWS::EC2::NatGateway"
                    },
                    "PRIVATEEGRESSVPC": {
                        "Properties": {
                            "CidrBlock": "172.16.0.0/20",
                            "EnableDnsHostnames": True,
                            "EnableDnsSupport": True,
                            "InstanceTenancy": "default",
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATEEGRESSVPC"
                                }
                            ]
                        },
                        "Type": "AWS::EC2::VPC"
                    },
                    "PerimeterInternal1": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.6.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal1"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "PerimeterInternal1SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "PerimeterInternal1SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "PerimeterInternal2": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.7.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal2"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "PerimeterInternal2SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "PerimeterInternal2SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "PerimeterInternal3": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.8.0/24",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PerimeterInternal3"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "PerimeterInternal3SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "PerimeterInternal3SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "PerimeterInternal3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "PublicRT": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PublicRT"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::RouteTable"
                    },
                    "PublicRTRoutePropagation": {
                        "DependsOn": [
                            "VPCGatewayAttachment"
                        ],
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
                        "Type": "AWS::EC2::VPNGatewayRoutePropagation"
                    },
                    "PublicRoute": {
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "PublicRouteIPv6": {
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "GatewayId": {
                                "Ref": "InternetGateway"
                            },
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "ReservedMgmt1": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.0/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt1"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedMgmt1SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedMgmt1SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "ReservedMgmt2": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.0/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt2"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedMgmt2SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedMgmt2SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "ReservedMgmt3": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.0/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedMgmt3"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedMgmt3SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "InternalSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedMgmt3SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            },
                            "SubnetId": {
                                "Ref": "ReservedMgmt3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "ReservedNet1": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    0,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.0.192/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet1"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedNet1SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedNet1SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet1"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "ReservedNet2": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    1,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.1.192/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet2"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedNet2SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedNet2SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet2"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "ReservedNet3": {
                        "DependsOn": "IPv6Block",
                        "Properties": {
                            "AssignIpv6AddressOnCreation": True,
                            "AvailabilityZone": {
                                "Fn::Select": [
                                    2,
                                    {
                                        "Fn::GetAZs": ""
                                    }
                                ]
                            },
                            "CidrBlock": "172.16.2.192/26",
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "ReservedNet3"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::Subnet"
                    },
                    "ReservedNet3SubnetNetworkACLAssociation": {
                        "Properties": {
                            "NetworkAclId": {
                                "Ref": "RestrictedSubnetAcl"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetNetworkAclAssociation"
                    },
                    "ReservedNet3SubnetRoutetableAssociation": {
                        "Properties": {
                            "RouteTableId": {
                                "Ref": "PublicRT"
                            },
                            "SubnetId": {
                                "Ref": "ReservedNet3"
                            }
                        },
                        "Type": "AWS::EC2::SubnetRouteTableAssociation"
                    },
                    "RestrictedSubnetAcl": {
                        "Properties": {
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "RestrictedSubnetAcl"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::NetworkAcl"
                    },
                    "RestrictedSubnetAclEntryIn": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInDNSTCP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInDNSUDP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInHTTP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInHTTPIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInHTTPS": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInHTTPSIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInNetBios": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInNetBios1": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInSquid2": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInTCPUnReserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInTCPUnReservedIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInUDPUnReserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryInUDPUnReservedIPv6": {
                        "Properties": {
                            "Egress": False,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryNTP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOut": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutDNSTCP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutDNSTCPIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutDNSUDP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutDNSUDPIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutHTTP": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutHTTPIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutHTTPS": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutHTTPSIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutNetBios": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutNetBios1": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutPuppet": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutSSH": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutSSHIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutTCPUnReservedIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReserved": {
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RestrictedSubnetAclEntryOutUDPUnReservedIPv6": {
                        "Properties": {
                            "Egress": True,
                            "Ipv6CidrBlock": "::/0",
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
                        },
                        "Type": "AWS::EC2::NetworkAclEntry"
                    },
                    "RouteNATGW1": {
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW1"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "RouteNATGW1IPv6": {
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT1"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "RouteNATGW2": {
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW2"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "RouteNATGW2IPv6": {
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT2"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "RouteNATGW3": {
                        "Properties": {
                            "DestinationCidrBlock": "0.0.0.0/0",
                            "NatGatewayId": {
                                "Ref": "NATGW3"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "RouteNATGW3IPv6": {
                        "Properties": {
                            "DestinationIpv6CidrBlock": "::/0",
                            "EgressOnlyInternetGatewayId": {
                                "Ref": "EgressGateway"
                            },
                            "RouteTableId": {
                                "Ref": "InternalRT3"
                            }
                        },
                        "Type": "AWS::EC2::Route"
                    },
                    "Test1TransitGWAttach": {
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW1"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 1"
                                }
                            ],
                            "TransitGatewayId": "tgw-01234567890123456",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::TransitGatewayAttachment"
                    },
                    "Test2TransitGWAttach": {
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
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "PRIVATE-EGRESS-VPC-TGW2"
                                },
                                {
                                    "Key": "Purpose",
                                    "Value": "Gateway Attach 2"
                                }
                            ],
                            "TransitGatewayId": "tgw-98765432109876543",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::TransitGatewayAttachment"
                    },
                    "VPCEndpoint": {
                        "Properties": {
                            "GroupDescription": "VPC Endpoint Interface Firewall Rules",
                            "GroupName": "VPCEndpoint",
                            "SecurityGroupEgress": [
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic",
                                    "FromPort": -1,
                                    "IpProtocol": "icmp",
                                    "ToPort": -1
                                },
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic",
                                    "FromPort": 0,
                                    "IpProtocol": "tcp",
                                    "ToPort": 65535
                                },
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic",
                                    "FromPort": 0,
                                    "IpProtocol": "udp",
                                    "ToPort": 65535
                                }
                            ],
                            "SecurityGroupIngress": [
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All ICMP Traffic",
                                    "FromPort": -1,
                                    "IpProtocol": "icmp",
                                    "ToPort": -1
                                },
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All TCP Traffic",
                                    "FromPort": 0,
                                    "IpProtocol": "tcp",
                                    "ToPort": 65535
                                },
                                {
                                    "CidrIp": "172.16.0.0/20",
                                    "Description": "All UDP Traffic",
                                    "FromPort": 0,
                                    "IpProtocol": "udp",
                                    "ToPort": 65535
                                }
                            ],
                            "Tags": [
                                {
                                    "Key": "Name",
                                    "Value": "VPCEndpoint"
                                }
                            ],
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::SecurityGroup"
                    },
                    "VPCFlowLogs": {
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
                        },
                        "Type": "AWS::EC2::FlowLog"
                    },
                    "VPCFlowLogsRole": {
                        "Properties": {
                            "AssumeRolePolicyDocument": {
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
                                ],
                                "Version": "2012-10-17"
                            },
                            "Path": "/",
                            "Policies": [
                                {
                                    "PolicyDocument": {
                                        "Statement": [
                                            {
                                                "Action": [
                                                    "logs:*"
                                                ],
                                                "Effect": "Allow",
                                                "Resource": "arn:aws:logs:*:*:*"
                                            }
                                        ],
                                        "Version": "2012-10-17"
                                    },
                                    "PolicyName": "root"
                                }
                            ]
                        },
                        "Type": "AWS::IAM::Role"
                    },
                    "VPCGatewayAttachment": {
                        "Properties": {
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            },
                            "VpnGatewayId": {
                                "Ref": "VGW"
                            }
                        },
                        "Type": "AWS::EC2::VPCGatewayAttachment"
                    },
                    "cloudformationEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "cloudtrailEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "codebuildEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "configEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "dynamodbEndPoint": {
                        "Properties": {
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
                            ],
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
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "ec2EndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "ec2messagesEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "elasticloadbalancingEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "eventsEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "executeapiEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "kinesisstreamsEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "kmsEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "logsEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "monitoringEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "s3EndPoint": {
                        "Properties": {
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
                            ],
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
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "sagemakerapiEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "sagemakerruntimeEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "secretsmanagerEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "servicecatalogEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "snsEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "ssmEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    },
                    "ssmmessagesEndPoint": {
                        "Properties": {
                            "PrivateDnsEnabled": True,
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
                            "VpcEndpointType": "Interface",
                            "VpcId": {
                                "Ref": "PRIVATEEGRESSVPC"
                            }
                        },
                        "Type": "AWS::EC2::VPCEndpoint"
                    }
                }
            },
            "requestId": "508122ef-6442-46eb-b2fc-5fab1f4f7064"
        }
        actual = src.macro.handler(transform_call, "")
        self.assertEquals(test_assert, actual)
