# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import requests
import unittest
import json
import HTMLTestRunner
import logging


class TestApi(unittest.TestCase):
    url = "http://fanyi.baidu.com/v2transapi"

    def setUp(self):
        print 'setup'

    def testChinese(self):
        print 'test1'
        params = {
            "from": "en",
            "to": "zh",
            "query": "study"
        }
        url = "http://fanyi.baidu.com/v2transapi"
        print 'url=', url
        r = requests.request("post", url, params=params)
        r = json.loads(r.text)
        # print (r)
        logging.info('sdsad')

    def testEn(self):
        print("test2")
        url = "http://fanyi.baidu.com/v2transapi"
        params = {
            "from": "zh",
            "to": "en",
            "query": "你好"
        }
        r = requests.request("post", url, params=params)
        print (r.text)
        data1 = r.json()['liju_result']['tag'][0]
        assert data1 == "hello", 'data1的值不等于hello'
        print (data1)

    def tearDown(self):
        print 'teardown'
        pass

if __name__ == "__main__":
    unittest.main()
# if __name__ == '__main__':
#     report_dir = r's.html'
#     re_open = open(report_dir, 'wb')
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestApi)
#     runner = HTMLTestRunner.HTMLTestRunner(
#         stream=re_open,
#         title=u'接口测试',
#         description=u'接口测试详情'
#     )
#     runner.run(suite)
#     re_open.close()
