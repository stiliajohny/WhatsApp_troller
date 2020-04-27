#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace below path with the absolute path
# to chromedriver in your computer

options = webdriver.ChromeOptions();
options.add_argument("user-data-dir=~/.chrome_driver_session")
# Create the folder. Change path accordingly

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 1000)


for x in range(0, 100):
    time.sleep(0.2)
    
    target = '"XXXXX"'

    string = "  " + " Hello @Shah "

    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    print("Printed " + str(x))

    default_input = "Type a message"
    # Change the Text with the default of the input-field

    inp_xpath = "//div[contains(.,'" + default_input + "')]"
    input_box = wait.until(EC.presence_of_element_located((By.XPATH, inp_xpath))).find_element_by_xpath('..')
    # input_box.send_keys(string)

    # If the Text is written in the input field, use this line:
    input_box.send_keys(string + str(x) + Keys.ENTER)
    time.sleep(0.1)
