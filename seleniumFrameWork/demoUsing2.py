"""
# File       : demoUsing2.py
# Time       : 10:04 AM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json

browser = webdriver.Chrome()
headers = {
    "name": "Request Cookies",
    "value": json.loads(open('cookies.json', 'r').read())['Request Cookies']
}
# browser.get('https://www.taobao.com')
# browser.add_cookie(headers)
# input_first = browser.find_element(By.ID, 'q')
# input_second = browser.find_element(By.CSS_SELECTOR, '#q')
# input_third = browser.find_element(By.XPATH, '//*[@id="q"]')
# input_fourth = browser.find_element(By.LINK_TEXT, '亲，请登录')
# input_fifth = browser.find_element(By.PARTIAL_LINK_TEXT, '请登录')
# input_sixth = browser.find_element(By.TAG_NAME, 'input')
# input_seventh = browser.find_element(By.CLASS_NAME, 'search-combobox-input')
# print(input_first, input_second, input_third, input_fourth, input_fifth, input_sixth, input_seventh, sep='')

# get kinds of data
# list = browser.find_elements(By.CSS_SELECTOR, '.service-bd li a')
# print([i.text for i in list], sep=' ')

# simulate action
# input = browser.find_element(By.ID, 'q')
# input.send_keys('iPhone')
# time.sleep(0.5)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element(By.CSS_SELECTOR, '.btn-search')
# print(button)
# button.click()

# simulate action Chains
# browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# browser.switch_to.frame('iframeResult')
# source = browser.find_element(By.ID, 'draggable')
# target = browser.find_element(By.ID, 'droppable')
# actions = webdriver.ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# run js codes
browser.get('https://www.zhihu.com/explore')
browser.execute_script('window.scrollTo(document.body.scrollHeight, 0)')
browser.execute_script('alert("To Bottom")')
# browser.close()
