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

    def test_base_natgw_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Name: PRIVATE-EGRESS-VPC, Template: VPC for private endpoints egress only}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            Endpoints:
                cloudformation:
                    Type: Interface
                    SubnetIds:
                      - ReservedMgmt1
                      - ReservedMgmt2
                      - ReservedMgmt3
                    SecurityGroupIds:
                      - VPCEndpoint
                dynamodb:
                    Type: Gateway
                    RouteTableIds:
                      - PublicRT
                      - InternalRT1
                      - InternalRT2
                      - InternalRT3
                    PolicyDocument: |
                        {
                            "Version":"2012-10-17",
                            "Statement":[
                                {
                                    "Effect":"Allow",
                                    "Principal": "*",
                                    "Action":["s3:*"],
                                    "Resource":["*"]
                                }
                            ]
                        }
        """)
        expected = {
            'dynamodbEndPoint': {
                'Type': 'AWS::EC2::VPCEndpoint',
                'Properties': {
                    'RouteTableIds': [{
                        'Ref': 'PublicRT'
                    }, {
                        'Ref': 'InternalRT1'
                    }, {
                        'Ref': 'InternalRT2'
                    }, {
                        'Ref': 'InternalRT3'
                    }],
                    'VpcEndpointType': 'Gateway',
                    'PolicyDocument': '{\n    "Version":"2012-10-17",\n    "Statement":[\n        {\n            "Effect":"Allow",\n            "Principal": "*",\n            "Action":["s3:*"],\n            "Resource":["*"]\n        }\n    ]\n}\n',
                    'ServiceName': {
                        'Fn::Join': ['', ['com.amazonaws.', {
                            'Ref': 'AWS::Region'
                        }, '.dynamodb']]
                    },
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    }
                }
            },
            'cloudformationEndPoint': {
                'Type': 'AWS::EC2::VPCEndpoint',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'SubnetIds': [{
                        'Ref': 'ReservedMgmt1'
                    }, {
                        'Ref': 'ReservedMgmt2'
                    }, {
                        'Ref': 'ReservedMgmt3'
                    }],
                    'SecurityGroupIds': [{
                        'Ref': 'VPCEndpoint'
                    }],
                    'ServiceName': {
                        'Fn::Join': ['', ['com.amazonaws.', {
                            'Ref': 'AWS::Region'
                        }, '.cloudformation']]
                    },
                    'PrivateDnsEnabled': True,
                    'VpcEndpointType': 'Interface'
                }
            }
        }
        actual, outputs = src.macro.buildVPCEndpoints(properties, resources, outputs)
        self.assertEquals(expected, actual)
