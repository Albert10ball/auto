# -*- coding: utf-8 -*-：
# -*-coding:gbk-*

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import WebDriverWait



class PythonOrgSearch1(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def test_timeSheet(
            self):
        browser = self.browser
        browser.maximize_window()
        browser.get("http://60.174.236.99:8090/cpm/#/")
        # self.assertIn("百度一下，你就知道", browser.title)
        # assert ("百度一下，你就知道" == browser.title)
        # time.sleep(10)
        # WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div/button/span[2]'))

        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath('//*[@id="username"]'))
        browser.find_element_by_xpath('//*[@id="username"]').send_keys("w2713")
        browser.find_element_by_xpath('//*[@id="password"]').send_keys("w2713")
        browser.find_element_by_id("rememberMe").click()
        browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div/div/form/button")\
            .click()
        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath('//*[@id="entity-menu"]'))
        browser.find_element_by_xpath('//*[@id="entity-menu"]').click()
        browser.find_element_by_xpath('/html/body/div[2]/nav/div/div[2]/ul/li[2]/ul/li/a').click()
        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div/button'))
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div/button').click()
        WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/button[2]'))
        # text = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[1]/td[8]').get_property('text')


        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[4]/input').clear()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[4]/input').send_keys(
            '8')
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[5]/input').clear()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[5]/input').send_keys(
            '8')
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[6]/input').clear()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[6]/input').send_keys(
            '8')
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[7]/input').clear()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[7]/input').send_keys(
            '8')
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[8]/input').clear()
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/div/table/tbody/tr[5]/td[8]/input').send_keys(
            '8')
        browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/form/button[2]').click()
        WebDriverWait(browser, 10).until(
            lambda browser: browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div[1]/div/div/div/button'))
        # browser.find_element_by_class_name('search_tool').click()
        # time.sleep(1)
        # browser.find_element_by_class_name('search_tool_la').click()
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="c-tips-container"]/div[1]/div/div/ul/li[2]/a').click()
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="container"]/div[2]/div/div[1]/span[1]').click()
        # time.sleep(1)
        # browser.find_element_by_xpath('//*[@id="4001"]/div[1]/h3/a[1]').click()
        #  time.sleep(4)
        # res = browser.find_element_by_xpath('//*[@id="header"]/div/div[2]/div[2]/div[3]/ul/li[7]/a')
        # res.click()
        # elem3 = browser.find_element_by_xpath('//*[@id="phoneId"]')
        # elem3.send_keys("15023579228")
        # button = browser.find_element_by_id('msgBtn')
        # button.click()
        # print ('ok')
        # print ("title is %s" % browser.title)
        # time.sleep(5)
        self.browser.close()

    def tearDown1(self):
        print ('关闭浏览器')
        self.browser.close()