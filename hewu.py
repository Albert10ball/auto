# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import unittest
import json
import time
import HTMLTestRunner
import sys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import selenium

reload(sys)
class LoginHeWu(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

        # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input').click()
        # time.sleep(5)
        # # WebDriverWait(browser, 10).until(lambda browser:browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[3]'))
        # browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[3]/span').click()
        # # select1.select_by_visible_text('穿戴钟表')
        # # Select(browser.find_element_by_class_name('el-input__inner')).select_by_visible_text('穿戴钟表')
        # # browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[3]').click()
        # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[2]/div[1]/input').click()
        # time.sleep(5)
        # browser.find_element_by_xpath('/html/body/div[8]/div/div[1]/ul/li').click()
        # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[3]/div[1]/input').click()
        # time.sleep(5)
        # browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[2]').click()
        # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[3]/div/div/label[1]/span[1]/span').click()
        # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[3]/span/button[1]').click()
        #
        # time.sleep(5)
        # print "12121"

    # def test_createProject(self):
    #     browser = self.browser
    #     browser.maximize_window()
    #     browser.get("http://172.19.3.186:22001/")
    #     browser.find_element_by_xpath('/html/body/header/div/div[2]/div[1]/div/div[1]/a[1]').click()
    #     browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[1]/div/div/input').send_keys("ren")
    #     browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[2]/div/div/input').send_keys(
    #         "11111111")
    #     browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[3]/div/div/input').send_keys("9999")
    #     time.sleep(1)
    #     WebDriverWait(self.browser, 5).until(lambda browser: browser.find_element_by_xpath(
    #         '/html/body/header/div/div[2]/div[2]/a[2]')).click()
    #     WebDriverWait(self.browser, 5).until(lambda browser: browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/nav/div/button/span')).click()
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[1]/div/div[1]/input').send_keys(
    #         'python')
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input').click()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath('/html/body/div[7]/div/div[1]/ul/li[1]/span').click()
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[2]/div[1]/input').click()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath('/html/body/div[8]/div/div[1]/ul/li[3]/span').click()
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[3]/div[1]/input').click()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[1]/span').click()
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[3]/div/div/label[1]/span[1]/span').click()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[4]/div/div/label[1]/span[1]/span').click()
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/div[1]/div/div[3]/span/button[1]/span').click()
    #     self.browser.refresh()
    #     time.sleep(1)
    #     article = self.browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/section/div/div[1]/div[1]/div/div')
    #     ActionChains(self.browser).move_to_element(article).perform()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/section/div/div[1]/div[1]/div/div/span[3]/i[3]').click()
    #     time.sleep(1)
    #     self.browser.find_element_by_xpath(
    #         '/html/body/div[5]/div/div[1]/section/div/div[4]/div/div[3]/div/button[1]/span').click()
    #     self.browser.refresh()
    #     time.sleep(2)
    #     self.browser.quit()

    def test_login_hewu(
            self):
        browser = self.browser
        browser.maximize_window()
        browser.get("http://172.19.3.186:22001/")
        browser.find_element_by_xpath('/html/body/header/div/div[2]/div[1]/div/div[1]/a[1]').click()
        browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[1]/div/div/input').send_keys("ren")
        browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[2]/div/div/input').send_keys(
            "11111111")
        browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[3]/div/div/input').send_keys("9999")
        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div/div/div[1]/form/button').click()
        WebDriverWait(browser, 10).until(lambda browser: browser.
                                         find_element_by_xpath('/html/body/header/div/div[2]/div[2]/a[2]'))
        browser.find_element_by_xpath('/html/body/header/div/div[2]/div[2]/a[2]').click()

        WebDriverWait(browser, 10).until(lambda browser: browser.
                                         find_element_by_xpath('/html/body/div[5]/div/div[1]/nav/div/button/span'))
        browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/nav/div/button/span').click()
        WebDriverWait(browser, 10).until(lambda browser: browser.
                                         find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/div[1]/div/div[3]/span/button[1]'))
        browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[1]/div/div/input'). \
            send_keys('P110')
        time.sleep(3)
        browser.find_element_by_xpath(
            '/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[1]/div[1]/input').click()

        time.sleep(1)
        browser.find_element_by_xpath('/html/body/div[9]/div/div[1]/ul/li[5]/span').click()  # 选择产品类别1
        browser.find_element_by_xpath(
            'html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[2]/div[1]/input').click()
        time.sleep(1)
        browser.find_element_by_xpath('html/body/div[8]/div/div[1]/ul[3]/span').click()  # 选择产品类别2
        browser.find_element_by_xpath(
            'html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[2]/div/div/div[3]/div[1]/input').click()
        time.sleep(1)
        browser.find_element_by_xpath('html/body/div[9]/div/div[1]/ul[1]/span').click()  # 选择产品类别3
        # print 111111
        # # browser = self.browser
        # # browser.find_element_by_xpath('/html/body/header/div/div[2]/div[2]/a[2]').click()
        # # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/nav/div/button').click()
        # # browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[1]/div/div/input')\
        # #     .send_keys("computer001")




    def tearDown(self):

        print ("完成，关闭浏览器")
        # self.browser.close()
        pass

if __name__ == "__main__":
    unittest.main()