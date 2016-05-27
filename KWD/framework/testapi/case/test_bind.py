# -*- coding: utf-8 -*-
import unittest
from ...tools.read_xml import ReadXML
from ..common.newuser import User
from ..common.merchantadd import MerchantAdd
from ..common.newusercheck import NewUserCheck


class TestBind(unittest.TestCase):
    u"""测试绑定BEST接口【R_Bind__User】"""
    def setUp(self):
        self.sheet_name = 'Bind'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)
        self.userid = User().signup()
        MerchantAdd(self.userid).addstep1()
        MerchantAdd(self.userid).addstep2()
        MerchantAdd(self.userid).addstep3()
        MerchantAdd(self.userid).approveapply(4)

    def test_bind(self):
        u"""测试绑定BEST接口【R_Bind__User】"""
        results = NewUserCheck(self.url, sheet_name=self.sheet_name, userid=self.userid).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
            if case['response'] == '{}':
                from ..common.merchantadd import MerchantAdd
                MerchantAdd(self.userid).unbind()
