# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestCheckCode(unittest.TestCase):
    u"""测试检查组织机构代码证是否被占用接口【P_Merchant__CheckCode】"""
    def setUp(self):
        self.sheet_name = 'CheckCode'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_checkcode(self):
        u"""测试检查组织机构代码证是否被占用接口【P_Merchant__CheckCode】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
