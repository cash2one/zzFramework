# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestGetBasicStatus(unittest.TestCase):
    u"""测试检查商户状态信息接口【P_Merchant__GetBasicStatus】"""
    def setUp(self):
        self.sheet_name = 'GetBasicStatus'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getbasicstatus(self):
        u"""测试检查商户状态信息接口【P_Merchant__GetBasicStatus】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
