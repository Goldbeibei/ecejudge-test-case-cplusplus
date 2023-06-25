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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    # Test name: login
    # Step # | name | target | value
    # 1 | open | https://120.101.8.132/ | 
    self.driver.get("https://120.101.8.132/")
    # 2 | setWindowSize | 968x1020 | 
    self.driver.set_window_size(968, 1020)
    # 3 | click | css=.ivu-btn-ghost > span | 
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-btn-ghost > span").click()
    # 4 | click | css=.ivu-input-type-text > .ivu-input | 
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-input-type-text > .ivu-input").click()
    # 5 | type | css=.ivu-input-type-text > .ivu-input | jefery
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-input-type-text > .ivu-input").send_keys("jefery")
    # 6 | click | css=.ivu-input-type-password > .ivu-input | 
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-input-type-password > .ivu-input").click()
    # 7 | type | css=.ivu-input-type-password > .ivu-input | jeferywbl
    self.driver.find_element(By.CSS_SELECTOR, ".ivu-input-type-password > .ivu-input").send_keys("jeferywbl")
    # 8 | click | css=.btn | 
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    # 9 | waitForElementPresent | css=.logo | 3000
    WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".logo")))
    # 10 | open | https://120.101.8.132/admin/ | 
    self.driver.get("https://120.101.8.132/admin/")
    # 11 | waitForElementPresent | css=.el-submenu:nth-child(4) > .el-submenu__title | 3000
    WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".el-submenu:nth-child(4) > .el-submenu__title")))
    # 12 | click | css=.el-submenu:nth-child(4) > .el-submenu__title | 
    self.driver.find_element(By.CSS_SELECTOR, ".el-submenu:nth-child(4) > .el-submenu__title").click()
    # 13 | waitForElementPresent | css=.is-active > font > font | 3000
    WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".is-active > font > font")))
    # 14 | click | css=.is-opened .el-menu-item:nth-child(2) > font > font | 
    self.driver.find_element(By.CSS_SELECTOR, ".is-opened .el-menu-item:nth-child(2) > font > font").click()
  