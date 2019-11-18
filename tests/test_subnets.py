import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderSubnetsSetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderSubnets(TestVPCBuilderSubnetsSetup):

    def test_base_subnets_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Template: VPC for private endpoints egress only, "info:environment": Staging, "info:owner": Versent}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            Subnets:
                ReservedMgmt1: {CIDR: 172.16.0.0/26, AZ: 0, NetACL: InternalSubnetAcl, RouteTable: InternalRT1, IPv6Iter: 0 }
                ReservedMgmt2: {CIDR: 172.16.1.0/26, AZ: 1, NetACL: InternalSubnetAcl, RouteTable: InternalRT2, IPv6Iter: 1 }
                ReservedMgmt3: {CIDR: 172.16.2.0/26, AZ: 2, NetACL: InternalSubnetAcl, RouteTable: InternalRT3, IPv6Iter: 2 }
        """, Loader=yaml.FullLoader)
        print(properties)
        expected = {
            'ReservedMgmt1': {
                'Type': 'AWS::EC2::Subnet',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [
                        {
                            'Value': 'ReservedMgmt1',
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
                    ],
                    'Ipv6CidrBlock': {
                        'Fn::Select': [0, {
                            'Fn::Cidr': [{
                                'Fn::Select': [0, {
                                    'Fn::GetAtt': ['PRIVATEEGRESSVPC', 'Ipv6CidrBlocks']
                                }]
                            }, 3, 64]
                        }]
                    },
                    'AvailabilityZone': {
                        'Fn::Select': [0, {
                            'Fn::GetAZs': ''
                        }]
                    },
                    'CidrBlock': '172.16.0.0/26',
                    'AssignIpv6AddressOnCreation': True
                },
                'DependsOn': 'IPv6Block'
            },
            'ReservedMgmt2': {
                'Type': 'AWS::EC2::Subnet',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [
                        {
                            'Value': 'ReservedMgmt2',
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
                    ],
                    'Ipv6CidrBlock': {
                        'Fn::Select': [1, {
                            'Fn::Cidr': [{
                                'Fn::Select': [0, {
                                    'Fn::GetAtt': ['PRIVATEEGRESSVPC', 'Ipv6CidrBlocks']
                                }]
                            }, 3, 64]
                        }]
                    },
                    'AvailabilityZone': {
                        'Fn::Select': [1, {
                            'Fn::GetAZs': ''
                        }]
                    },
                    'CidrBlock': '172.16.1.0/26',
                    'AssignIpv6AddressOnCreation': True
                },
                'DependsOn': 'IPv6Block'
            },
            'ReservedMgmt3': {
                'Type': 'AWS::EC2::Subnet',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [
                        {
                            'Value': 'ReservedMgmt3',
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
                    ],
                    'Ipv6CidrBlock': {
                        'Fn::Select': [2, {
                            'Fn::Cidr': [{
                                'Fn::Select': [0, {
                                    'Fn::GetAtt': ['PRIVATEEGRESSVPC', 'Ipv6CidrBlocks']
                                }]
                            }, 3, 64]
                        }]
                    },
                    'AvailabilityZone': {
                        'Fn::Select': [2, {
                            'Fn::GetAZs': ''
                        }]
                    },
                    'CidrBlock': '172.16.2.0/26',
                    'AssignIpv6AddressOnCreation': True
                },
                'DependsOn': 'IPv6Block'
            },
            'ReservedMgmt3SubnetRoutetableAssociation': {
                'Type': 'AWS::EC2::SubnetRouteTableAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt3'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT3'
                    }
                }
            },
            'ReservedMgmt3SubnetNetworkACLAssociation': {
                'Type': 'AWS::EC2::SubnetNetworkAclAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt3'
                    },
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    }
                }
            },
            'ReservedMgmt1SubnetNetworkACLAssociation': {
                'Type': 'AWS::EC2::SubnetNetworkAclAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt1'
                    },
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    }
                }
            },
            'ReservedMgmt2SubnetNetworkACLAssociation': {
                'Type': 'AWS::EC2::SubnetNetworkAclAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt2'
                    },
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    }
                }
            },
            'ReservedMgmt1SubnetRoutetableAssociation': {
                'Type': 'AWS::EC2::SubnetRouteTableAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt1'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT1'
                    }
                }
            },
            'ReservedMgmt2SubnetRoutetableAssociation': {
                'Type': 'AWS::EC2::SubnetRouteTableAssociation',
                'Properties': {
                    'SubnetId': {
                        'Ref': 'ReservedMgmt2'
                    },
                    'RouteTableId': {
                        'Ref': 'InternalRT2'
                    }
                }
            }
        }
        actual, outputs = src.macro.buildSubnets(properties, resources, outputs, parameters={})
        self.assertEquals(expected, actual)
