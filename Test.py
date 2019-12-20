"""
Written By Jennifer Dixon For Amy from Cover
"""

import os
import selenium
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
import unittest

""""
Test Methods
"""

def setUp():
    driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
    driver.implicitly_wait(15)  # Wait 15 seconds for web browser to open
    driver.get("https://www.monkeyuser.com/")

def view_rand_comic():
    driver.find_element_by_xpath("//div[@class='thumb random nobefore']/a").click()
    driver.implicitly_wait(10)
    assert "No results found" not in driver.page_source

def tearDown():
    driver.close()


driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.implicitly_wait(15)  # Wait 15 seconds for web browser to open
driver.get("https://www.monkeyuser.com/")


view_rand_comic()
tearDown()
