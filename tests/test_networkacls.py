import unittest
import json
import yaml

import src.macro
from mock import MagicMock


class TestVPCBuilderNetworkACLSetup(unittest.TestCase):
    identifier = 'TEST'

    def setUp(self):
        self.maxDiff = None


class TestVPCBuilderNetworkACL(TestVPCBuilderNetworkACLSetup):

    def test_base_networkacl_object(self):
        resources = {}
        outputs = {}
        properties = yaml.load("""\
            CIDR: 172.16.0.0/20
            Details: {VPCName: PRIVATEEGRESSVPC, VPCDesc: Private Egress VPC, Region: ap-southeast-2, IPv6: True}
            Tags: {Name: PRIVATE-EGRESS-VPC, Template: VPC for private endpoints egress only}
            DHCP: {Name: DhcpOptions, DNSServers: 172.16.0.2, NTPServers: 169.254.169.123, NTBType: 2}
            NetworkACLs:
                RestrictedSubnetAcl:
                    RestrictedSubnetAclEntryInTCPUnReserved: '90,6,allow,false,0.0.0.0/0,1024,65535'
                    RestrictedSubnetAclEntryInUDPUnReserved: '91,17,allow,false,0.0.0.0/0,1024,65535'
                    RestrictedSubnetAclEntryInTCPUnReservedIPv6: '92,6,allow,false,::/0,1024,65535'
                    RestrictedSubnetAclEntryInUDPUnReservedIPv6: '93,17,allow,false,::/0,1024,65535'
                    RestrictedSubnetAclEntryOutTCPUnReserved: '90,6,allow,true,0.0.0.0/0,1024,65535'
                    RestrictedSubnetAclEntryOutUDPUnReserved: '91,17,allow,true,0.0.0.0/0,1024,65535'
                    RestrictedSubnetAclEntryOutTCPUnReservedIPv6: '92,6,allow,true,::/0,1024,65535'
                    RestrictedSubnetAclEntryOutUDPUnReservedIPv6: '93,17,allow,true,::/0,1024,65535'
                InternalSubnetAcl:
                    InternalSubnetAclEntryIn: '100,-1,allow,false,172.16.0.0/16,1,65535'
                    InternalSubnetAclEntryOut: '100,-1,allow,true,172.16.0.0/16,1,65535'
                    InternalSubnetAclEntryInTCPUnreserved: '102,6,allow,false,0.0.0.0/0,1024,65535'
                    InternalSubnetAclEntryInUDPUnreserved: '103,17,allow,false,0.0.0.0/0,1024,65535'
                    InternalSubnetAclEntryInTCPUnreservedIPv6: '104,6,allow,false,::/0,1024,65535'
                    InternalSubnetAclEntryInUDPUnreservedIPv6: '105,17,allow,false,::/0,1024,65535'
        """)
        expected = {
            'RestrictedSubnetAclEntryInTCPUnReserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 90,
                    'Protocol': 6,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': False,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'RestrictedSubnetAclEntryInUDPUnReserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 91,
                    'Protocol': 17,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': False,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'InternalSubnetAclEntryInUDPUnreserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 103,
                    'Protocol': 17,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': False,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'RestrictedSubnetAcl': {
                'Type': 'AWS::EC2::NetworkAcl',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'RestrictedSubnetAcl',
                        'Key': 'Name'
                    }]
                }
            },
            'RestrictedSubnetAclEntryOutTCPUnReserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 90,
                    'Protocol': 6,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': True,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'InternalSubnetAcl': {
                'Type': 'AWS::EC2::NetworkAcl',
                'Properties': {
                    'VpcId': {
                        'Ref': 'PRIVATEEGRESSVPC'
                    },
                    'Tags': [{
                        'Value': 'InternalSubnetAcl',
                        'Key': 'Name'
                    }]
                }
            },
            'RestrictedSubnetAclEntryOutTCPUnReservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 92,
                    'Protocol': 6,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': True,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'RestrictedSubnetAclEntryOutUDPUnReserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 91,
                    'Protocol': 17,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': True,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'RestrictedSubnetAclEntryInUDPUnReservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 93,
                    'Protocol': 17,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': False,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'InternalSubnetAclEntryInTCPUnreservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 104,
                    'Protocol': 6,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': False,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'RestrictedSubnetAclEntryInTCPUnReservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 92,
                    'Protocol': 6,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': False,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'InternalSubnetAclEntryInUDPUnreservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 105,
                    'Protocol': 17,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': False,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'RestrictedSubnetAclEntryOutUDPUnReservedIPv6': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'RestrictedSubnetAcl'
                    },
                    'RuleNumber': 93,
                    'Protocol': 17,
                    'Ipv6CidrBlock': '::/0',
                    'Egress': True,
                    'RuleAction': 'allow',
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    }
                }
            },
            'InternalSubnetAclEntryIn': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 100,
                    'Protocol': -1,
                    'PortRange': {
                        'To': 65535,
                        'From': 1
                    },
                    'Egress': False,
                    'RuleAction': 'allow',
                    'CidrBlock': '172.16.0.0/16'
                }
            },
            'InternalSubnetAclEntryInTCPUnreserved': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 102,
                    'Protocol': 6,
                    'PortRange': {
                        'To': 65535,
                        'From': 1024
                    },
                    'Egress': False,
                    'RuleAction': 'allow',
                    'CidrBlock': '0.0.0.0/0'
                }
            },
            'InternalSubnetAclEntryOut': {
                'Type': 'AWS::EC2::NetworkAclEntry',
                'Properties': {
                    'NetworkAclId': {
                        'Ref': 'InternalSubnetAcl'
                    },
                    'RuleNumber': 100,
                    'Protocol': -1,
                    'PortRange': {
                        'To': 65535,
                        'From': 1
                    },
                    'Egress': True,
                    'RuleAction': 'allow',
                    'CidrBlock': '172.16.0.0/16'
                }
            }
        }
        actual, outputs = src.macro.buildNetworlACLs(properties, resources, outputs)
        self.assertEquals(expected, actual)
