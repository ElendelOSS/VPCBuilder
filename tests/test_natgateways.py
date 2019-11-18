import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderNATGatewaySetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderNATGateway(TestVPCBuilderNATGatewaySetup):

    def test_base_natgw_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Template: VPC for private endpoints egress only, "info:environment": Staging, "info:owner": Versent}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            NATGateways:
                NATGW1:
                    {Subnet: ReservedNet1, Routetable: InternalRT1}
                NATGW2:
                    {Subnet: ReservedNet2, Routetable: InternalRT2}
                NATGW3:
                    {Subnet: ReservedNet3, Routetable: InternalRT3}
        """, Loader=yaml.FullLoader)
        expected = {
            'InternalRT1NATGW1': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW1'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT1'
                    }
                }
            },
            'InternalRT3NATGW3': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW3'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT3'
                    }
                }
            },
            'InternalRT2NATGW2': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW2'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT2'
                    }
                }
            },
            'InternalRT2NATGW2IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT2'
                    }
                }
            },
            'NATGW3': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet3'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW3', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW3',
                            'Key': 'Name'
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
            'NATGW2': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet2'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW2', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW2',
                            'Key': 'Name'
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
            'NATGW1': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet1'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW1', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW1',
                            'Key': 'Name'
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
            'EIPNATGW2': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'EIPNATGW3': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'EIPNATGW1': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'InternalRT3NATGW3IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT3'
                    }
                }
            },
            'InternalRT1NATGW1IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT1'
                    }
                }
            }
        }
        actual, outputs = src.macro.buildNATGateways(properties, resources, outputs, parameters={})
        self.assertEquals(expected, actual)

    def test_multi_routetable_natgw_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Template: VPC for private endpoints egress only, "info:environment": Staging, "info:owner": Versent}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            NATGateways:
                NATGW1:
                    Subnet: ReservedNet1
                    Routetable:
                    - InternalRT1
                    - ProxyRT1
                NATGW2:
                    {Subnet: ReservedNet2, Routetable: InternalRT2}
                NATGW3:
                    {Subnet: ReservedNet3, Routetable: InternalRT3}
        """, Loader=yaml.FullLoader)
        expected = {
            'InternalRT1NATGW1': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW1'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT1'
                    }
                }
            },
            'ProxyRT1NATGW1': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW1'
                    },
                    'RouteTableId': {
                        'Ref': 'ProxyRT1'
                    }
                }
            },
            'InternalRT3NATGW3': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW3'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT3'
                    }
                }
            },
            'InternalRT2NATGW2': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'NatGatewayId': {
                        'Ref': 'NATGW2'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT2'
                    }
                }
            },
            'InternalRT2NATGW2IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT2'
                    }
                }
            },
            'NATGW3': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet3'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW3', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW3',
                            'Key': 'Name'
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
            'NATGW2': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet2'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW2', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW2',
                            'Key': 'Name'
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
            'NATGW1': {
                'Type': 'AWS::EC2::NatGateway',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedNet1'
                    },
                    'AllocationId': {
                        'Fn::GetAtt': ['EIPNATGW1', 'AllocationId']
                    },
                    'Tags': [
                        {
                            'Value': 'NATGW1',
                            'Key': 'Name'
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
            'EIPNATGW2': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'EIPNATGW3': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'EIPNATGW1': {
                'Type': 'AWS::EC2::EIP',
                'Properties': {
                    'Domain': 'vpc'
                }
            },
            'InternalRT3NATGW3IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT3'
                    }
                }
            },
            'InternalRT1NATGW1IPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'EgressOnlyInternetGatewayId': {
                        'Ref': 'EgressGateway'
                    },
                    'DestinationIpv6CidrBlock': '::/0',
                    'RouteTableId': {
                        'Ref': 'InternalRT1'
                    }
                }
            },
            "ProxyRT1NATGW1IPv6": {
                "Properties": {
                    "DestinationIpv6CidrBlock": "::/0",
                    "EgressOnlyInternetGatewayId": {
                        "Ref": "EgressGateway"
                    },
                    "RouteTableId": {
                        "Ref": "ProxyRT1"
                    }
                },
                "Type": "AWS::EC2::Route"
            }
        }
        actual, outputs = src.macro.buildNATGateways(properties, resources, outputs, parameters={})
        print(json.dumps(actual, sort_keys=True))
        print("###")
        print(json.dumps(expected, sort_keys=True))
        self.assertEquals(expected, actual)
