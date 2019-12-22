"""
Written By Jennifer Dixon For Amy from Cover
"""

import os
import selenium
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
import unittest

""""
Feature Tests
  - 1) Views a random comic
  - 2) Views the latest comic
  - 3) User can view the next comic


#To Do Improvements - Future work that would improve the overall effectiveness of the test itself, can find more bugs
#To Do Enhancements - Future work that would add more features that could be during the test
"""


def view_rand_comic():
    """
    Test 1)
    Feature: User can view a random comic
    Test: Is the 'random' button available, if so, does it work?
    Input: find 'Random' comic button and click it
    Pass Criteria (ALL): 'Random' button is available, no assert error, new url is different than old
    FaiL Criteria (One or more): 'Random' button is unavailable, page displays no results
    Test Limitations: 'Random' button class must be 'thumb random nobefore', uses webpage navigation links
    """
    print("Test 1 - View Random Comic")
    old_url = driver.current_url
    driver.find_element_by_xpath("//div[@class='thumb random nobefore']/a").click()
    driver.implicitly_wait(10)
    new_url = driver.current_url
    assert "No results found" not in driver.page_source
    if old_url == new_url: #Assumption: We assume that if URLs are different, viewed comic is different
        print("FAIL Random Comic button produced same comic.\n")
    else:
        print("PASS Random Comic view completed. Random Comic button produced different comic.\n")

    # ToDo Improvement: check both random buttons, not just first
    # ToDo Improvement: Screenshot pages before and after, use image library to compare and verify comics are different
    # ToDo Improvement: Loop clicking random button and count how many times comics appear same or different.
    #   True Randomness means there is a small probability that the user will land on the same comic after clicking
    #   the random button. Collect data on how often this happens and analyze if it falls within acceptable statistical
    #   probability.

def view_latest_comic():
    """
    Test 2)
    Feature: User can view the latest comic
    Test: Is the 'latest' button available, if so, does it work?
    Input: find latest comic button and click it
    Pass Criteria (ALL): 'Last comic' button is available, no assert error, new url is different than old
    FaiL Criteria (One or more): 'last comic' button is unavailable, page displays no results
    Test Limitations: Test will produce a false fail if it starts on last comic.
    """
    print("Test 2 - View Latest Comic")
    old_url = driver.current_url
    driver.find_element_by_xpath("//div[@class='thumb last']/a").click()
    new_url = driver.current_url
    assert "No results found" not in driver.page_source
    if old_url == new_url: #Assumption: We assume that if URLs are different, viewed comic is different
        print("FAIL Unable to view latest comic.\n")
    else:
        print("PASS Latest Comic view completed.\n")

    #ToDo Improvement: Amend test criteria so navigating FROM latest comic To Latest comic still passes

def able_view_next_comic():
    """
    Test 3)
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
    print("Test 3 - User can view next comic")
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
            print("FAIL Did not navigate to next comic\n")
        else:
            print("PASS Navigated to next comic\n")
        #ToDo Improvement: check both next comic buttons, not just first
        #ToDo Improvement: Check that the new comic is the "Next" Comic

def tearDown():
    driver.close()

#Setup
driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe"))
driver.implicitly_wait(15)  # Wait 15 seconds for web browser to open
driver.get("https://www.monkeyuser.com/")

#Sample Test Script
view_rand_comic()
view_latest_comic()
driver.find_element_by_xpath("//div[@class='thumb random nobefore']/a").click()
able_view_next_comic()
tearDown()
