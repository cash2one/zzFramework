# -*- coding: utf-8 -*-
import unittest
from ..common.basecheck import BaseCheck
from ...tools.read_xml import ReadXML


class TestAddUser(unittest.TestCase):
    u"""测试用户注册接口【P_User__AddUser】"""
    def setUp(self):
        self.sheet_name = 'AddUser'
        self.url = ReadXML('zhigou.xml').get_url(self.sheet_name)

    def test_adduser(self):
        u"""测试用户注册接口【P_User__AddUser】"""
        results = BaseCheck(self.url, sheet_name=self.sheet_name).docase()
        for case in results:
            print case['index'], case['params'], case['response'], case['code']
            self.assertIn(case['code'], case['response'])
