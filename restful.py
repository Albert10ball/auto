# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import requests
import json
import unittest
import HTMLTestRunner
# 接口url



# 参数
class TestWealth(unittest.TestCase):
    def setUp(self):
        print 'setup'

    def testWealth(self):

        url = "http://fanyi.baidu.com/v2transapi"
        params = {
            "from": "en",
            "to": "zh",
            "query": "test"
        }
        # 发送接口命令
        r = requests.request("post", url, params=params)
        # 打印结果
        print(r.text)
        r1 = json.dumps(r.text)
        print (r1)
        r2 = json.loads(r1)
        print (r2)

    def tearDown(self):
        print 'teardown'
        pass

if __name__ == "__main__":
    unittest.main()
# if __name__ == '__main__':
#     report_dir = r's.html'
#     re_open = open(report_dir, 'wb')
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestWealth)
#     runner = HTMLTestRunner.HTMLTestRunner(
#         stream=re_open,
#         title=u'接口测试',
#         description=u'接口测试详情'
#     )
#     runner.run(suite)
#     re_open.close()