#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.southwest.com/air/check-in/index.html")

# TODO: Input your information here!! ------------------------------------------------------------------------
confirmation_number = "your_confirmation_number"
first_name = "your_first_name"
last_name = "your_last_name"
# ------------------------------------------------------------------------------------------------------------

# Login to site using credentials
confirmation_input = driver.find_element_by_id("confirmationNumber")
confirmation_input.send_keys(confirmation_number)

first_name_input = driver.find_element_by_id("passengerFirstName")
first_name_input.send_keys(first_name)

last_name_input = driver.find_element_by_id("passengerLastName")
last_name_input.send_keys(last_name)

check_in_button = driver.find_element_by_id("form-mixin--submit-button")
check_in_button.click()

# Handle MFA