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
    """
    Feature: User can view a random comic using random comic feature
    Test: Is the 'Random' button available, if so, does it work?
    Input: find the random comic button and click it
    Expected output: User can navigate to a random comic
    Pass Criteria (ALL): 'Random' button is available, no assert error, new url is different than old
    FaiL Criteria (One or more): 'Random' button is unavailable, page displays no results
    Test Limitations: 'Next' button class must be 'thumb random nobefore', uses webpage navigation links
    """

    old_url = driver.current_url
    driver.find_element_by_xpath("//div[@class='thumb random nobefore']/a").click()
    driver.implicitly_wait(10)
    new_url = driver.current_url
    assert "No results found" not in driver.page_source
    if old_url == new_url: #Assumption: We assume that if URLs are different, viewed comic is different
        print("View completed. Random Comic button produced same comic.")
    else:
        print("View completed. Random Comic button produced different comic.")

    # ToDo Improvement: check both random buttons, not just first
    # ToDo Improvement: Screenshot pages before and after, use image library to compare and verify comics are different
    # ToDo Imnprovement: Loop clicking random button and count how many times comics appear same or different.
    #   True Randomness means there is a small probability that the user will land on the same comic after clicking
    #   the random button. Collect data on how often this happens and analyze if it falls within acceptable statistical
    #   probability.

def able_view_next_comic():
    """
    Feature: User can view the next comic
    Test: Is the 'next comic' button available, if so, does it work?
    Input: find next comic button and click it
    Expected output: User can navigate to next comic
    Pass Criteria (ALL): 'Next' button is available, no assert error, old url is different than new url
    Fail Criteria (One or more): 'Next' button is unavailable (likely because its the last one),
        page url does not change, page displays no results
    Test Limitations: 'Next' button class must be 'thumb next nobefore', uses webpage navigation links,
        does not check if new comic is the "next" comic only that urls are different
    """
    nextbuttonlist = driver.find_elements_by_xpath("//div[@class='thumb next nobefore']/a")
    if nextbuttonlist == []:
        print("View Next Comic Button Unavailable")
    else:
        print("View Next Comic Button is available")
        #Case: If next button available, test click
        old_url = driver.current_url
        driver.find_element_by_xpath("//div[@class='thumb next nobefore']/a").click()
        driver.implicitly_wait(10)
        new_url = driver.current_url
        assert "No results found" not in driver.page_source
        if old_url == new_url:  # Assumption: We assume that if URLs are different, it correctly navigated to NEXT comic
            print("FAIL Did not navigated to next comic.")
        else:
            print("PASS Navigated to next comic")
        #ToDo Improvement: check both next comic buttons, not just first
        #ToDo Improvement: Check that the new comic is the "Next" Comic

def tearDown():
    driver.close()


driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.implicitly_wait(15)  # Wait 15 seconds for web browser to open
driver.get("https://www.monkeyuser.com/")


view_rand_comic()
able_view_next_comic()
tearDown()
