"""
# File       : collectTaobaoGoods.py
# Time       : 5:47 PM
# Author     : vincent
# version    : python 3.8
# Description:
"""
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
import pymongo

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
KEYWORD = 'ipad'


def index_page(page):
    print("It's climbing the ", page, 'page')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_goods()
    except TimeoutException:
        index_page(page)


def get_goods():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    product = {}
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text()[:-3],
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
    save_to_mongo(product)


MONGO_URL = 'mongodb+srv://vincent:ZTXic3344@tempcluster.kslgvab.mongodb.net/?retryWrites=true&w=majority'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'goods'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def save_to_mongo(result):
    try:
        if db[MONGO_COLLECTION].insert_one(result):
            print("Save to mongoDB successfully!")
    except Exception:
        print("Save to mongoDB failed!")


if __name__ == '__main__':
    MAX_PAGE = 5
    for i in range(1, MAX_PAGE + 1):
        sleep(0.5)
        index_page(i)
# Path: seleniumFrameworkAdvancedActions/collectTaobaoGoods.py