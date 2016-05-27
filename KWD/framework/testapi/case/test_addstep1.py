# -*- coding: utf-8 -*-
import unittest
from ..common.newuser import User
from ..common.newusercheck import NewUserCheck
from ...tools.read_xml import ReadXML


class TestAddStep1(unittest.TestCase):
    u"""测试商户入驻第一步的接口【P_Merchant__AddStep1】"""
    def setUp(self):
        self.sheet_name = 'AddStep1'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)
        self.userid = User().signup()

    def test_addstep1(self):
        u"""测试商户入驻第一步的接口【P_Merchant__AddStep1】"""
        results = NewUserCheck(self.url, sheet_name=self.sheet_name, userid=self.userid).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])

