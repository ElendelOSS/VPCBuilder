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
            Tags: {Name: PRIVATE-EGRESS-VPC, Template: VPC for private endpoints egress only}
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
        """)
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
                    'Tags': [{
                        'Value': 'PRIVATE-EGRESS-VPC-TGW2',
                        'Key': 'Name'
                    }, {
                        'Value': 'Gateway Attach 2',
                        'Key': 'Purpose'
                    }]
                }
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
                    'Tags': [{
                        'Value': 'PRIVATE-EGRESS-VPC-TGW1',
                        'Key': 'Name'
                    }, {
                        'Value': 'Gateway Attach 1',
                        'Key': 'Purpose'
                    }]
                }
            }
        }
        actual, outputs = src.macro.buildTransitGateways(properties, resources, outputs)
        self.assertEquals(expected, actual)
