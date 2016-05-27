# -*- coding: utf-8 -*-
from selenium import webdriver
from .path import TOOLS_PATH


def open_browser(browser, url):
    """browser是浏览器编号：
    FireFox  1
    Chrome   2
    IE       3
    如果不是1,2,3，返回None"""
    if browser == 1:
        driver = webdriver.Firefox()
    elif browser == 2:
        driver = webdriver.Chrome(TOOLS_PATH + 'browsertools\\chromedriver.exe')
    elif browser == 3:
        driver = webdriver.Ie(TOOLS_PATH + 'browsertools\\IEDriverServer.exe')
    else:
        return None
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(30)
    return driver

if __name__ == '__main__':
    bd = 'https://www.baidu.com'
    dr = open_browser(3, bd)
    import time
    time.sleep(2)
    dr.quit()