
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

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://60.174.236.99:8090/cpm/#/")
# self.assertIn("百度一下，你就知道", browser.title)
# assert ("百度一下，你就知道" == browser.title)
time.sleep(10)
elem = browser.find_element_by_id("username")
elem.send_keys("w2713")
browser.find_element_by_id("password").send_keys("w2713")
browser.find_element_by_id("rememberMe").click()
browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div/div/form/button').click()
time.sleep(2)
