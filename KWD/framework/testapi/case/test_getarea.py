# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestGetArea(unittest.TestCase):
    u"""测试获取所在地接口【P_User__GetArea】"""
    def setUp(self):
        self.sheet_name = 'GetArea'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_getarea(self):
        u"""测试获取所在地接口【P_User__GetArea】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
