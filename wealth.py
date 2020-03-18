# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import json
import requests
import uniout
import unittest

class TestWealth(unittest.TestCase):
    def setUp(self):
        print 'setup'

    def testWealth(self):
        r = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=秀山')
        print (u'数据类型:', type(r.text), r.text)
        hh = json.dumps(r.text)
        print (u'数据类型：', type(hh),hh)

    def tearDown(self):
        print 'teardown'
        pass

if __name__ == "__main__":
    unittest.main()
