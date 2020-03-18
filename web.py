# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
import unittest  # 加载unittest模块
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import json
import time
import HTMLTestRunner
import sys
import selenium

reload(sys)

sys.setdefaultencoding('utf8')


class PythonOrgSearch1(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_search_in_python_org1(
            self):
        browser = self.browser
        browser.maximize_window()
        browser.get("http://www.baidu.com")
        self.assertIn("百度一下，你就知道", browser.title)
        assert ("百度一下，你就知道" == browser.title)

        elem = browser.find_element_by_name("wd")
        elem.send_keys("selenium")
        elem1 = browser.find_element_by_id("su")
        elem1.click()
        time.sleep(4)
        browser.find_element_by_class_name('search_tool').click()
        time.sleep(1)
        browser.find_element_by_class_name('search_tool_la').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="c-tips-container"]/div[1]/div/div/ul/li[2]/a').click()
        time.sleep(1)
        browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/span[1]').click()
        time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').click()
        #  time.sleep(4)
        # res = browser.find_element_by_xpath('//*[@id="header"]/div/div[2]/div[2]/div[3]/ul/li[7]/a')
        # res.click()
        # elem3 = browser.find_element_by_xpath('//*[@id="phoneId"]')
        # elem3.send_keys("15023579228")
        # button = browser.find_element_by_id('msgBtn')
        # button.click()
        print ('ok')
        print ("title is %s" % browser.title)
        time.sleep(5)
        self.browser.close()

    def tearDown1(self):
        print ('关闭浏览器')
        self.browser.close()


# class PythonOrgSearch2(unittest.TestCase):
#     def setUp(self):
#         self.browser = webdriver.Chrome()
#
#     def test_search_in_python_org2(self):
#         browser = self.browser
#         browser.get("http://www.python.org")
#         self.assertIn("Python", browser.title)
#         # print ("title is %s"%browser.title)
#         elem = browser.find_element_by_name("q")
#         elem.send_keys("selenium")
#         elem.send_keys(Keys.RETURN)
#         self.assertIn("Selenium", browser.title)
#
#     def tearDown2(self):
#         self.browser.close()



if __name__ == '__main__':
    unittest.main()
