# Generated by Selenium IDE
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestSmokeside:
    def setup_method(self, method):
        options = Options()
        options.add_argument("--headless=new")
        self.driver = webdriver.Chrome(options=options)
        self.vars = {}
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_smokeside(self):
        self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
        self.driver.set_window_size(1918, 1030)
        
        # Check site logo
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
        assert len(elements) > 0
        
        # Verify header
        element = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Directory")))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        
        assert self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-title > h1"))).text == "Teton Idaho"
        assert self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-title > h2"))).text == "Chamber of Commerce"
        
        # Navigate to Join Us page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home"))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Join Us!")))
        elements = self.driver.find_elements(By.LINK_TEXT, "Join Us!")
        assert len(elements) > 0
        
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Join Us!"))).click()
        
        # Check Directory and Members
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Directory"))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, "directory-grid"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member:nth-child(9)")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9)")
        assert len(elements) > 0
        
        self.wait.until(EC.element_to_be_clickable((By.ID, "directory-list"))).click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)")
        assert len(elements) > 0
        
        # Join form
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Join"))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME, "fname")))
        elements = self.driver.find_elements(By.NAME, "fname")
        assert len(elements) > 0
        
        self.driver.find_element(By.NAME, "fname").send_keys("f")
        self.driver.find_element(By.NAME, "lname").send_keys("f")
        self.driver.find_element(By.NAME, "bizname").send_keys("f")
        self.driver.find_element(By.NAME, "biztitle").send_keys("f")
        self.driver.find_element(By.NAME, "submit").click()
        
        # Verify email field
        self.wait.until(EC.presence_of_element_located((By.NAME, "email")))
        elements = self.driver.find_elements(By.NAME, "email")
        assert len(elements) > 0
        
        # Admin login
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))).click()
        self.wait.until(EC.presence_of_element_located((By.ID, "username")))
        self.driver.find_element(By.ID, "username").send_keys("grsraider66@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("zCZYk8znjkCeag4")
        self.driver.find_element(By.CSS_SELECTOR, ".admin-main").click()
        self.driver.find_element(By.ID, "password").clear()
        self.driver.find_element(By.ID, "password").send_keys("f")
        self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
        
        # Verify login error
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".errorMessage")))
        assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
        assert self.driver.title == "Teton Idaho CoC"
        
        # Check main spotlight and other spotlights
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".main-spotlight")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".main-spotlight")
        assert len(elements) > 0

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".spotlight1")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1")
        assert len(elements) > 0

        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".spotlight2")))
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2")
        assert len(elements) > 0
