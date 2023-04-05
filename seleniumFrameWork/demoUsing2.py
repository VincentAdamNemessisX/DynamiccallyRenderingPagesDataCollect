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
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

browser = webdriver.Chrome()
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
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# get data
# browser.get('https://www.zhihu.com/explore')
# logo = browser.find_element(By.CLASS_NAME, 'css-1hlrcxk')
# print(logo)
# print(logo.get_attribute('fill'))
# quest = browser.find_element(By.CLASS_NAME, 'css-1nd7dqm')
# print(quest.text)

# get id, location, tag name, size
# browser.get('https://www.zhihu.com/explore')
# # with open('test.html', 'w') as f:
# #     f.write(browser.page_source)
# input = browser.find_element(By.CLASS_NAME, 'SearchBar-searchButton')
# print(input.text.encode(''))
# print(input.id)
# print(input.location)
# print(input.tag_name)
# print(input.size)

# change frame
# browser.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
# browser.switch_to.frame('iframeResult')
# try:
#     logo = browser.find_element(By.CLASS_NAME, 'logo')
# except NoSuchElementException:
#     print('No logo')
# browser.switch_to.parent_frame()
# logo = browser.find_element(By.CLASS_NAME, 'logo')
# print(logo)
# print(logo.text)

# delay wait
# hide-wait
# browser.implicitly_wait(5)  # default value is 0
# browser.get('https://www.zhihu.com/explore')
# input = browser.find_elements(By.CLASS_NAME, 'ExploreSpecialCard-contentTitle')
# print([i.text for i in input])

# no-hide-wait
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 5)  # it just was give a max time to wait, but not a fixed time, if the element is found, it will stop waiting
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# forward and back
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# time.sleep(1)

# cookies
# browser.get('https://www.taobao.com')
# print(browser.get_cookies())
# # browser.add_cookie({'name': 'name', 'domain': 'www.zhihu.com', 'value': 'germey'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# cookies = open('cookies.json', 'r').read()
# cookies = json.loads(cookies)
# browser.add_cookie(cookies)
# print(browser.get_cookies())

# option management
# browser.get('https://www.baidu.com')
# browser.execute_script('window.open()')
# print(browser.window_handles)
# browser.switch_to.window(browser.window_handles[1])
# browser.get('https://www.taobao.com')
# time.sleep(1)
# browser.switch_to.window(browser.window_handles[0])
# browser.get('https://python.org')

# exception handle
try:
    browser.get('https://www.baidu.com')
except TimeoutException:
    print('Time out')
try:
    browser.find_element(By.ID, 'hello')
except NoSuchElementException:
    print('No such element')
browser.quit()
