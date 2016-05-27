# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestGetApplyList(unittest.TestCase):
    u"""测试获取商家入驻申请资料接口【P_Merchant__GetApplyList】"""
    def setUp(self):
        self.sheet_name = 'GetApplyList'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getapplylist(self):
        u"""测试获取商家入驻申请资料接口【P_Merchant__GetApplyList】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
