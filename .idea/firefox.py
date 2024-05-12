import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

driver = webdriver.Firefox()
driver.get("https://whatismyip.com")

driver.save_screenshot("screenshot.png")
time.sleep(15)
driver.quit()