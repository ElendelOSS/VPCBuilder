import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderTransitGatewaySetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderTransitGateway(TestVPCBuilderTransitGatewaySetup):

    def test_base_transitgw_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Template: VPC for private endpoints egress only, "info:environment": Staging, "info:owner": Versent}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            TransitGateways:
              Test1:
                TransitGatewayId: tgw-01234567890123456
                Tags: {Name: PRIVATE-EGRESS-VPC-TGW1, Purpose: Gateway Attach 1}
                Subnets:
                  - Internal1
                  - Internal2
                  - Internal3
              Test2:
                TransitGatewayId: tgw-98765432109876543
                Tags: {Name: PRIVATE-EGRESS-VPC-TGW2, Purpose: Gateway Attach 2}
                Subnets:
                  - Internal1
                  - Internal2
                  - Internal3
                RouteTables:
                    InternalRT1:
                    - RouteName: Internal1
                      RouteCIDR: 10.0.0.0/8
                    - RouteName: Internal2
                      RouteCIDR: 192.168.0.0/16
                    InternalRT2:
                    - RouteName: Internal1
                      RouteCIDR: 10.0.0.0/8
                    - RouteName: Internal2
                      RouteCIDR: 192.168.0.0/16
                    InternalRT3:
                    - RouteName: Internal1
                      RouteCIDR: 10.0.0.0/8
                    - RouteName: Internal2
                      RouteCIDR: 192.168.0.0/16
        """, Loader=yaml.FullLoader)
        expected = {
            'Test2TransitGWAttach': {
                'Type': 'AWS::EC2::TransitGatewayAttachment',
                'Properties': {
                    'SubnetIds': [{
                        'Ref': 'Internal1'
                    }, {
                        'Ref': 'Internal2'
                    }, {
                        'Ref': 'Internal3'
                    }],
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'TransitGatewayId': 'tgw-98765432109876543',
                    'Tags': [
                        {
                            'Value': 'PRIVATE-EGRESS-VPC-TGW2',
                            'Key': 'Name'
                        },
                        {
                            'Value': 'Gateway Attach 2',
                            'Key': 'Purpose'
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
            'Test1TransitGWAttach': {
                'Type': 'AWS::EC2::TransitGatewayAttachment',
                'Properties': {
                    'SubnetIds': [{
                        'Ref': 'Internal1'
                    }, {
                        'Ref': 'Internal2'
                    }, {
                        'Ref': 'Internal3'
                    }],
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'TransitGatewayId': 'tgw-01234567890123456',
                    'Tags': [
                        {
                            'Value': 'PRIVATE-EGRESS-VPC-TGW1',
                            'Key': 'Name'
                        },
                        {
                            'Value': 'Gateway Attach 1',
                            'Key': 'Purpose'
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
            }
        }
        actual, outputs = src.macro.buildTransitGateways(properties, resources, outputs, parameters={})
        print(json.dumps(actual))
        print(json.dumps(expected))
        self.assertEquals(expected, actual)
