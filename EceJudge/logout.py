# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 避免跳出不安全網站
from selenium.webdriver.chrome.options import Options




class TestUntitled():
  def setup_method(self, method):
    # 避免跳出不安全網站
    options = Options()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    # self.driver.quit()
    print("Error")
   
  def test_logout(self):
    # Test name: logout
    # Step # | name | target | value
    # 1 | open | https://120.101.8.132/ | 
    self.driver.get("https://120.101.8.132/")
    # 2 | setWindowSize | 968x1020 | 
    self.driver.set_window_size(968, 1020)
    # 設置隱式等待時間為3秒
    self.driver.implicitly_wait(3)
    # 3 | click | css=.ivu-icon-md-arrow-dropdown | 
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-icon-md-arrow-dropdown").click()
    # 設置隱式等待時間為3秒
    self.driver.implicitly_wait(3)
    # 4 | click | css=.ivu-dropdown-item-divided | 
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-dropdown-item-divided").click()

