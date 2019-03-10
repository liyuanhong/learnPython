#coding:utf-8
'''
学习基于selenium的网页爬虫
'''
import re
from selenium import webdriver


_url = "https://www.toutiao.com/a6620277507927048717/"


def getChromeOptions():
    chrome_options = webdriver.ChromeOptions()
    # 设置无界面化运行
    chrome_options.add_argument('--headless')
    return chrome_options

#获取网页文彬
def getHtml():
    driver.get(_url)
    html = driver.page_source
    return html

#获取网页中的文章
def getArticle(html):
    arti = re.findall(r'class="article-box">(.+)<div class="bui-box article-tag',html)
    return arti

def getDriver():
    '''
    指定chrome webdriver的位置
    chrome webDriver api 详见：https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.chrome.webdriver
    chrome webDriver下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads
    '''
    driver = webdriver.Chrome(executable_path=r"./chromedriver",
                              chrome_options=chrome_options)
    return driver



chrome_options = getChromeOptions()
driver = getDriver()
html = getHtml()
arti = getArticle(html)
driver.close()
print arti[0]