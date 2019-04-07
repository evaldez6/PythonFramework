import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Python0rgSearch(unittest.TestCase):
    
    def setUp(self):
        
        firefox_profile = webdriver.FirefoxProfile()

        firefox_profile.set_preference("browser.privatebrowsing.autostart", True)
        
        self.driver = webdriver.Firefox(firefox_profile=firefox_profile, 
            executable_path='../Utilities/BrowserDrivers/geckodriver.exe')
        
    def test_search_with_python_org(self):
        driver = self.driver
        driver.get("http://www.google.es")
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pi")
        time.sleep(3)
        elem.send_keys(Keys.RETURN)
        time.sleep(5)
        driver.find_element_by_xpath("//span[contains(text(),'3.14159265359')]")
        print("Busqueda exitosa")
        
    def tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.close()