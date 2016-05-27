# -*- coding: utf-8 -*-
import unittest
from ...tools.read_xml import ReadXML
from ..common.newuser import User
from ..common.merchantadd import MerchantAdd
from ..common.newusercheck import NewUserCheck


class TestAddStep3(unittest.TestCase):
    u"""测试商户入驻第三步接口【P_Merchant__AddStep3】"""
    def setUp(self):
        self.sheet_name = 'AddStep3'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)
        self.userid = User().signup()
        MerchantAdd(self.userid).addstep1()
        MerchantAdd(self.userid).addstep2()

    def test_addstep3(self):
        u"""测试商户入驻第三步接口【P_Merchant__AddStep3】"""
        results = NewUserCheck(self.url, sheet_name=self.sheet_name, userid=self.userid).docase3()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
