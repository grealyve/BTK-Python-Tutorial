from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)

searchInput = driver.find_element_by_name("q")
# searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source   # Kaynak kodunu bs4 olarak çekebilirsin böyle.

result = driver.find_elements_by_class_name("v-align-middle")

for element in result:
    print(element.text)

driver.close()