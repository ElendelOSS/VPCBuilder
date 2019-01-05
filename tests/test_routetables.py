import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderRouteTablesSetup(unittest.TestCase):
    identifier = 'TEST'

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderRouteTables(TestVPCBuilderRouteTablesSetup):

    def test_base_routetable_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Name: PRIVATE-EGRESS-VPC, Template: VPC for private endpoints egress only}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            RouteTables:
                PublicRT:
                  - RouteName: PublicRoute
                    RouteCIDR: 0.0.0.0/0
                    RouteGW: InternetGateway
                  - RouteName: PublicRouteIPv6
                    RouteCIDR: ::/0
                    RouteGW: InternetGateway
                InternalRT1:
                InternalRT2:
                InternalRT3:
        """)
        expected = {
            'InternalRT2': {
                'Type': 'AWS::EC2::RouteTable',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'InternalRT2',
                        'Key': 'Name'
                    }]
                }
            },
            'PublicRouteIPv6': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'GatewayId': {
                        'Ref': 'InternetGateway'
                    },
                    'RouteTableId': {
                        'Ref': 'PublicRT'
                    },
                    'DestinationIpv6CidrBlock': '::/0'
                }
            },
            'PublicRoute': {
                'Type': 'AWS::EC2::Route',
                'Properties': {
                    'GatewayId': {
                        'Ref': 'InternetGateway'
                    },
                    'DestinationCidrBlock': '0.0.0.0/0',
                    'RouteTableId': {
                        'Ref': 'PublicRT'
                    }
                }
            },
            'InternalRT1RoutePropagation': {
                'Type': 'AWS::EC2::VPNGatewayRoutePropagation',
                'Properties': {
                    'RouteTableIds': [{
                        'Ref': 'InternalRT1'
                    }],
                    'VpnGatewayId': {
                        'Ref': 'VGW'
                    }
                },
                'DependsOn': ['VPCGatewayAttachment']
            },
            'InternalRT1': {
                'Type': 'AWS::EC2::RouteTable',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'InternalRT1',
                        'Key': 'Name'
                    }]
                }
            },
            'InternalRT3RoutePropagation': {
                'Type': 'AWS::EC2::VPNGatewayRoutePropagation',
                'Properties': {
                    'RouteTableIds': [{
                        'Ref': 'InternalRT3'
                    }],
                    'VpnGatewayId': {
                        'Ref': 'VGW'
                    }
                },
                'DependsOn': ['VPCGatewayAttachment']
            },
            'PublicRT': {
                'Type': 'AWS::EC2::RouteTable',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'PublicRT',
                        'Key': 'Name'
                    }]
                }
            },
            'PublicRTRoutePropagation': {
                'Type': 'AWS::EC2::VPNGatewayRoutePropagation',
                'Properties': {
                    'RouteTableIds': [{
                        'Ref': 'PublicRT'
                    }],
                    'VpnGatewayId': {
                        'Ref': 'VGW'
                    }
                },
                'DependsOn': ['VPCGatewayAttachment']
            },
            'InternalRT3': {
                'Type': 'AWS::EC2::RouteTable',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'InternalRT3',
                        'Key': 'Name'
                    }]
                }
            },
            'InternalRT2RoutePropagation': {
                'Type': 'AWS::EC2::VPNGatewayRoutePropagation',
                'Properties': {
                    'RouteTableIds': [{
                        'Ref': 'InternalRT2'
                    }],
                    'VpnGatewayId': {
                        'Ref': 'VGW'
                    }
                },
                'DependsOn': ['VPCGatewayAttachment']
            }
        }
        actual, outputs = src.macro.buildRouteTables(properties, resources, outputs)
        self.assertEquals(expected, actual)
