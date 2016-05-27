# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestCheckName(unittest.TestCase):
    u"""测试检查企业名称是否被占用接口【P_Merchant__CheckName】"""
    def setUp(self):
        self.sheet_name = 'CheckName'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_checkname(self):
        u"""测试检查企业名称是否被占用接口【P_Merchant__CheckName】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
