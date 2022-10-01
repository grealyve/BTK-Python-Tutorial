from selenium import webdriver
import time

driver = webdriver.Firefox()
url = "http://github.com"
driver.get(url)             # site açılır

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.com-homepage.png")

url = "http://github.com/grealyve"
driver.get(url)

print(driver.title)

if "grealyve" in driver.title:
    driver.save_screenshot("github.com-grealyve.png")

driver.back()
# driver.forward()
time.sleep(2)

driver.close()