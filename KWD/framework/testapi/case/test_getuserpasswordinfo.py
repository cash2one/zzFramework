# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestGetUserPasswordInfo(unittest.TestCase):
    u"""测试验证用户登录密码接口【P_User__GetUserPasswordInfo】"""
    def setUp(self):
        self.sheet_name = 'GetUserPasswordInfo'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getuserpasswordinfo(self):
        u"""测试验证用户登录密码接口【P_User__GetUserPasswordInfo】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
