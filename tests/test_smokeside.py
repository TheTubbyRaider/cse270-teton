# Generated by Selenium IDE
import pytest
import time
import json
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSmokeside():
  def setup_method(self, method):
    options = Options()
    options.add_argument("--headless=new")
    self.driver = webdriver.Chrome(options=options)
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_smokeside(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1918, 1030)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    element = self.driver.find_element(By.LINK_TEXT, "Directory")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    self.driver.find_element(By.LINK_TEXT, "Home").click()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, "body")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Directory").click()
    self.driver.find_element(By.ID, "directory-grid").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "directory-list").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join").click()
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").click()
    self.driver.find_element(By.NAME, "fname").send_keys("f")
    self.driver.find_element(By.NAME, "lname").click()
    self.driver.find_element(By.NAME, "lname").send_keys("f")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("f")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("f")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Admin").click()
    self.driver.find_element(By.ID, "username").send_keys("grsraider66@gmail.com")
    self.driver.find_element(By.ID, "password").send_keys("zCZYk8znjkCeag4")
    self.driver.find_element(By.CSS_SELECTOR, ".admin-main").click()
    self.driver.find_element(By.ID, "password").send_keys("f")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
    assert self.driver.title == "Teton Idaho CoC"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".main-spotlight")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
    assert len(elements) > 0
  
