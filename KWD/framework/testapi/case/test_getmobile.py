# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestGetMobile(unittest.TestCase):
    u"""测试检查手机号是否被占用接口【P_User__GetMobile】"""
    def setUp(self):
        self.sheet_name = 'GetMobile'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getmobile(self):
        u"""测试检查手机号是否被占用接口【P_User__GetMobile】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
