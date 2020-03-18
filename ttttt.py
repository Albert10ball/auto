import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window()
browser.get("http://172.19.3.186:22001/")
browser.find_element_by_xpath('/html/body/header/div/div[2]/div[1]/div/div[1]/a[1]').click()
browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[1]/div/div/input').send_keys("ren")
browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[2]/div/div/input').send_keys(
            "11111111")
browser.find_element_by_xpath('/html/body/div/div/div[1]/form/div[1]/div[3]/div/div/input').send_keys()
time.sleep(10)
browser.find_element_by_xpath('/html/body/div/div/div[1]/form/button').click()
ele = WebDriverWait(10, webdriver).until(EC.presence_of_all_elements_located(By.XPATH, '/html/body/header/div/div[2]/div[2]/a[2]'))
ele = browser.find_element_by_xpath('/html/body/header/div/div[2]/div[2]/a[2]')
ele.click()
browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/nav/div/button').click()
browser.find_element_by_xpath('/html/body/div[5]/div/div[1]/div[1]/div/div[2]/form/div[1]/div/div/input')\
            .send_keys("computer001")
