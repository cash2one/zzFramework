# -*- coding: utf-8 -*-
from KWD.framework.testapi.common import merchantadd
from KWD.framework.testapi.common import newuser
from KWD.framework.tools.HTMLTestRunner import HTMLTestRunner
from KWD.framework.tools.config import Config
import datetime

from KWD.framework.testapi.suite.test_suite import suite

if __name__ == '__main__':
    # 注册新用户
    # user = newuser.User().signup()
    #
    # # 商户入驻
    # merchant = merchantadd.MerchantAdd(user)
    # merchant.addstep1()
    # merchant.addstep2()
    # merchant.addstep3()
    # merchant.approveapply(4)
    # merchant.bind()
    # merchant.openshop()

    # filename = Config().get('report', 'path') + 'report-{0}.html'.format(datetime.date.today())
    # fp = file(filename, 'wb')
    # runner = HTMLTestRunner(stream=fp, title=u'直购接口测试报告', description='Test_Report')
    # runner.run(suite())

    from KWD.framework.testapi.case.test_addstep3 import TestAddStep3
    import unittest
    unittest.main()
