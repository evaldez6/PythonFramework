from selenium import webdriver
import time

def OpenBrowser():
    pass
firefox_profile = webdriver.FirefoxProfile()

firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

driver = webdriver.Firefox(firefox_profile=firefox_profile, 
    executable_path='../Utilities/BrowserDrivers/geckodriver.exe')
driver.maximize_window()
time.sleep(3)

def gotowebsite():
    pass

driver.get("https://www.codecademy.com/")
time.sleep(5)

def CloseBrowser():
    pass

driver.delete_all_cookies()
driver.close()

