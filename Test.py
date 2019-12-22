"""
Written By Jennifer Dixon For Amy from Cover
"""

import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select


""""
Feature Tests
  - 1) Views a random comic
  - 2) Views the latest comic
  - 3) User can view the next comic
  - 4) Views the history of comics
  - 5) Opens the comics from the following dates:
    - December 4, 2018
    - June 19, 2018
    - May 30, 2017
  - 6) Verify a product can be added to cart
  - 7) Verify the checkout screen functions correctly excluding the checkout button

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

    #ToDo Improvement: Revisit test pass criteria so navigating FROM latest comic To Latest comic passes

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

def view_comic_history():

    """
    Test 4)
    Feature: Views the history of comics
    Test: Can the user navigate to the "Comics List" page?
    Input: Click and navigate to the Comics List page
    Expected output: User can navigate to Comics list page
    Pass Criteria (ALL): 'Comics list' button is available, Comics history page has "Table of contents" for title
    Fail Criteria (One or more): 'Comics List' button is unavailable, page displays no results, title of page is
        not "Table of contents"
    Test Limitations: Assumes that comic history will always be on Comics List page where titled "Table of contents"
    """

    print("Test 4 - Views the history of comics")
    driver.find_element_by_id("list").click()
    driver.implicitly_wait(10)
    assert "No results found" not in driver.page_source #Fail Condition
    ComicHistory = driver.title
    if ComicHistory=="Table of contents":
        print("PASS Comic history Table of Contents page loaded\n")
    else:
        print("FAIL Table of contents title not found\n")


def open_comic_by_date(SearchDateText):
    """"
    Test 5)
    Feature: Opens the comics from the following dates:
    - December 4, 2018
    - June 19, 2018
    - May 30, 2017
    Test: Can the following comics be found by date and opened?
    Input: Navigate and find comics of given date
    Output: Comic of given date is viewed
    Pass Criteria (ALL): Comic of given date is found
    Fail Criteria (One or more): Comic of given date is not found
    Test Limitations: relies on correctly functioning "first comic" and "next comic" navigation buttons, relies on lack of "next"
                    button indicating end of comic library. Will search only first 250 comics (arbitrary). Requires input Format must be "DD MMM YYYY",
                     Input format is CASE SENSITIVE. Will open only first comic with input date (does not work for multiple comics from same day).
    """
    print("Test 5 - Open Comic from the following date: " + SearchDateText)
    driver.get("https://www.monkeyuser.com/")
    driver.find_element_by_xpath("//div[@class='thumb initial']/a").click()

    for x in range(250):
        nextbuttonlist = driver.find_elements_by_xpath("//div[@class='thumb next nobefore']/a")
        ComicDateElement = driver.find_element_by_tag_name("time")
        ComicDate = ComicDateElement.text

        if nextbuttonlist == []:
            print("FAIL " + SearchDateText + " Comic not found\n")
            break
        elif ComicDate == SearchDateText:
            print("PASS " + SearchDateText + " Comic Is Available\n")
            break
        else:
            driver.find_element_by_xpath("//div[@class='thumb next nobefore']/a").click()

    # ToDO Improvement: Stop searching early by comparing input date to webpage date so it doesn't iterate through
    #       all the comics once it passes the expected date area
    # ToDo Improvement: Screenshot the comic once found, for further verification that the correct one was found

def add_to_cart():
    """
    Test 6)
    Feature: a product can be added to cart
    Input: Navigate to shopping item and add to cart
    Output: viewed cart, A product must be in cart
    Pass criteria: Cart header is loaded and there is item in cart
    Fail Criteria: Cart is empty
    Test Limitations: Cart must be empty before test begins in order to be valid.
        Does not check that the correct item was added to cart. Only checks if cart header is present, not item added
    """
    print("Test 6 - Verify a product can be added to cart")
    driver.get("https://www.monkeyuser.com/")
    driver.find_element_by_partial_link_text("SHOP").click()
    assert "No results found" not in driver.page_source  # Fail Condition
    driver.find_element_by_partial_link_text("Feature").click()
    assert "No results found" not in driver.page_source  # Fail Condition
    driver.find_element_by_name("add").click()
    assert "No results found" not in driver.page_source  # Fail Condition
    cartlist=driver.find_elements_by_xpath("//div[@class='cart-header']/a")
    if cartlist == []:
        print("FAIL Nothing in cart\n")
    else:
        print("PASS Added to cart\n")

    #ToDo Improvement: Generalize test to clear cart/check if empty before adding something to cart
    #ToDO Enhancement: Add verification that correct item (ex: Developer plushie) was added to cart
    #ToDO Enhancement: Verify the correct quantity was added to cart

def verify_checkout():
    """
    Test 7)
    Feature: Checkout screen functions correctly excluding checkout button
    Author Note: From prompt, "Checkout" screen is interpreted as the information screen after "continue to checkout"
    Input: Navigate to checkout screen and input shipping data, signup for marketing
    Output: Checkout information filled
    Pass Criteria: Shipping information accepts keys
    Fail Criteria: Page displays no results, Shipping fields do not accept keys
    Limitations: Test does not vary shipping information inputted or optional/required fields. Checkout pages usually
        check if the required fields are filled correctly.
    """
    print("Test 7 - Verify checkout screen")
    driver.get("https://www.monkeyuser.com/")
    driver.find_element_by_partial_link_text("SHOP").click()
    driver.find_element_by_partial_link_text("Feature").click()
    driver.find_element_by_name("add").click()
    driver.find_element_by_name("checkout").click()
    assert "No results found" not in driver.page_source  # Fail Condition

    driver.find_element_by_id("checkout_buyer_accepts_marketing").click()
    #driver.find_element_by_id("checkout_buyer_accepts_marketing").click()

    driver.find_element_by_id("checkout_email_or_phone").send_keys("64799999999")
    driver.find_element_by_name("checkout[shipping_address][first_name]").send_keys("Marilyn")
    driver.find_element_by_name("checkout[shipping_address][last_name]").send_keys("Monroe")
    driver.find_element_by_id("checkout_shipping_address_company").send_keys("The Misfits")
    driver.find_element_by_id("checkout_shipping_address_address1").send_keys("12305 Fifth Helena Drive")
    driver.find_element_by_id("checkout_shipping_address_address2").send_keys("Apt 1")
    driver.find_element_by_id("checkout_shipping_address_city").send_keys("Brentwood, Los Angeles")

    select1=Select(driver.find_element_by_id("checkout_shipping_address_country"))
    select1.select_by_visible_text("United States")
    select2=Select(driver.find_element_by_id("checkout_shipping_address_province"))
    select2.select_by_visible_text("California")
    driver.find_element_by_id("checkout_shipping_address_zip").send_keys("90049")

    driver.find_element_by_id("checkout_remember_me").click()
    #driver.find_element_by_id("checkout_remember_me").click()

    print("PASS Checkout screen accepts shipping information and marketing\n")

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
view_comic_history()
open_comic_by_date("04 DEC 2018") #Format must be "DD MMM YYYY", CASE SENSITIVE
open_comic_by_date("19 JUN 2018") #Will open the first 19 Jun 2018 comic
open_comic_by_date("30 MAY 2017")
add_to_cart()
verify_checkout()
tearDown()
