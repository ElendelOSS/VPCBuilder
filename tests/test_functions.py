import unittest
import json

import src.macro
from mock import MagicMock


class TestVPCBuilderFunctionsSetup(unittest.TestCase):
    identifier = "TEST"

    def setUp(self):
        None


class TestVPCBuilderFunctions(TestVPCBuilderFunctionsSetup):

    def test_isIPV6Cidr_ipv6defaultroute(self):
        ipv6_default = "::/0"
        test_assert = "Ipv6CidrBlock"
        actual = src.macro.isIPv6NetACL(ipv6_default)
        self.assertEquals(test_assert, actual)

    def test_isIPV6Cidr_ipv4defaultroute(self):
        ipv4_default = "0.0.0.0/0"
        test_assert = "CidrBlock"
        actual = src.macro.isIPv6NetACL(ipv4_default)
        self.assertEquals(test_assert, actual)

    def test_isIPv6Route_ipv6defaultroute(self):
        ipv6_default = "::/0"
        test_assert = "DestinationIpv6CidrBlock"
        actual = src.macro.isIPv6Route(ipv6_default)
        self.assertEquals(test_assert, actual)

    def test_isIPv6Route_ipv4defaultroute(self):
        ipv4_default = "0.0.0.0/0"
        test_assert = "DestinationCidrBlock"
        actual = src.macro.isIPv6Route(ipv4_default)
        self.assertEquals(test_assert, actual)
