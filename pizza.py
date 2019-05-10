#!/usr/bin/python3

import time
import getpass
from selenium import webdriver


browser = webdriver.Chrome(executable_path=r"C:\Users\spadajo\PycharmProjects\VZPYANA\chromedriver.exe")

browser.get("https://www.dominos.com/en/pages/customer/#!/customer/login/")

time.sleep(3)

useremailElm = browser.find_element_by_xpath('//*[@id="Email"]')
useremailElm.send_keys('rzfeeserspam@gmail.com')

passElm = browser.find_element_by_xpath('//*[@id="Password"]')
passElm.send_keys('PizzaPie123')

browser.find_element_by_xpath('//*[@id="customerLoginPage"]/div/div/div[2]/div/form/div[14]/div[1]/button').click()

time.sleep(3)

lockElm = browser.find_element_by_xpath

time.sleep(3)

stateElm = browser.find_element_by_name('Region')
stateElm.send_keys('CO')