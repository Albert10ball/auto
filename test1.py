# -*- coding: utf-8 -*-：
# -*-coding:gbk-*
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

browser = webdriver.Chrome()
browser.get('http://mail.163.com/')   # 进入163邮箱登录界面
assert "http://mail.163.com/" in browser.current_url
# WebDriverWait(browser, 10).until(lambda browser: browser.find_element_by_name('email'))
elem = browser.find_element_by_name('email').clear()   # 清空用户名的输入框
elem.send_keys("15023579228")
browser.find_element_by_name('password').send_keys('YIzl@321')
browser.find_element_by_id('dologin').click()  # 这里也可以像用户名那里一样赋值给一个变量然后加一行代码：elem.send_keys(Keys.RETURN)
