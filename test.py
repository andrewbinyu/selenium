#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:55:23 2018

@author: binyu
"""

from selenium import webdriver
import time
#from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument("--headless")       # define headless


#driver = webdriver.Chrome('/usr/local/bin/chromedriver')     # open Chrome browser
driver = webdriver.Chrome('/usr/local/bin/chromedriver', options=chrome_options) # without opening browser

driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.get_screenshot_as_file("./screenshot1.png")
#time.sleep(2)
driver.find_element_by_link_text("About").click()
driver.get_screenshot_as_file("./screenshot2.png")
#time.sleep(2)
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

# 得到网页 html, 还能截图
#html = driver.page_source       # get html
#driver.get_screenshot_as_file("./screenshot1.png")
#driver.close()