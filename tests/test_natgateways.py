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
            Tags: {Name: PRIVATE-EGRESS-VPC, Template: VPC for private endpoints egress only}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            NATGateways:
                NATGW1:
                    {Subnet: ReservedNet1, Routetable: InternalRT1}
                NATGW2:
                    {Subnet: ReservedNet2, Routetable: InternalRT2}
                NATGW3:
                    {Subnet: ReservedNet3, Routetable: InternalRT3}
        """)
        expected = {
            'RouteNATGW1': {
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
            'RouteNATGW3': {
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
            'RouteNATGW2': {
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
            'RouteNATGW2IPv6': {
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
                    'Tags': [{
                        'Value': 'NATGW3',
                        'Key': 'Name'
                    }]
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
                    'Tags': [{
                        'Value': 'NATGW2',
                        'Key': 'Name'
                    }]
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
                    'Tags': [{
                        'Value': 'NATGW1',
                        'Key': 'Name'
                    }]
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
            'RouteNATGW3IPv6': {
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
            'RouteNATGW1IPv6': {
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
        actual, outputs = src.macro.buildNATGateways(properties, resources, outputs)
        self.assertEquals(expected, actual)
