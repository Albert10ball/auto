# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import unittest
# 加载模块

import time
import HTMLTestRunner
import api_test
import web
import restful
import wealth

testUnit = unittest.TestSuite()

testUnit.addTest(unittest.makeSuite(api_test.TestApi))
testUnit.addTest(unittest.makeSuite(restful.TestWealth))
testUnit.addTest(unittest.makeSuite(web.PythonOrgSearch1))
testUnit.addTest(unittest.makeSuite(wealth.TestWealth))
now = time.strftime("%m-%d %H_%m_%S", time.localtime())
print (now)
report_dir = r'result.html'
re_open = open(now+report_dir, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(
    stream=re_open,
    title=u'接口测试',
    description=u'接口测试详情',
    tester=u'wangjianlin'
)
runner.run(testUnit)
re_open.close()
