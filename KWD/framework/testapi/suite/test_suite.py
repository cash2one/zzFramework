#coding:utf-8
import unittest


def suite():
    u"""组合所有商家入驻接口的suite"""
    testsuite = unittest.TestSuite()
    from ..case import test_checkcode, test_checkname, test_getapplylist, test_getarea, test_getbasicstatus,\
        test_getmobile, test_getuserpasswordinfo, test_addstep1, test_addstep2, test_addstep3, test_adduser,\
        test_bind, test_openshop, test_unbind
    testsuite.addTest(test_checkcode.TestCheckCode("test_checkcode"))
    testsuite.addTest(test_checkname.TestCheckName("test_checkname"))
    testsuite.addTest(test_getapplylist.TestGetApplyList("test_getapplylist"))
    testsuite.addTest(test_getarea.TestGetArea("test_getarea"))
    testsuite.addTest(test_getbasicstatus.TestGetBasicStatus("test_getbasicstatus"))
    testsuite.addTest(test_getmobile.TestGetMobile("test_getmobile"))
    testsuite.addTest(test_getuserpasswordinfo.TestGetUserPasswordInfo("test_getuserpasswordinfo"))
    testsuite.addTest(test_addstep1.TestAddStep1("test_addstep1"))
    testsuite.addTest(test_addstep2.TestAddStep2("test_addstep2"))
    testsuite.addTest(test_addstep3.TestAddStep3("test_addstep3"))
    testsuite.addTest(test_adduser.TestAddUser("test_adduser"))
    testsuite.addTest(test_bind.TestBind("test_bind"))
    testsuite.addTest(test_openshop.TestOpenShop("test_openshop"))
    testsuite.addTest(test_unbind.TestUnBind("test_unbind"))
    return testsuite

