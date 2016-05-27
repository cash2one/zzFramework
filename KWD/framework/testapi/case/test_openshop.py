# -*- coding: utf-8 -*-
import unittest
from ...tools.read_xml import ReadXML
from ..common.newuser import User
from ..common.merchantadd import MerchantAdd
from ..common.newusercheck import NewUserCheck


class TestOpenShop(unittest.TestCase):
    u"""测试开通店铺接口【P_Merchant__OpenShop】"""
    def setUp(self):
        self.sheet_name = 'OpenShop'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)
        self.userid = User().signup()
        MerchantAdd(self.userid).addstep1()
        MerchantAdd(self.userid).addstep2()
        MerchantAdd(self.userid).addstep3()
        MerchantAdd(self.userid).approveapply(4)
        MerchantAdd(self.userid).bind()

    def test_openshop(self):
        u"""测试开通店铺接口【P_Merchant__OpenShop】"""
        results = NewUserCheck(self.url, sheet_name=self.sheet_name, userid=self.userid).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
