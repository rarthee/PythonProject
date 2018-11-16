import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.maximize_window()
driver.get("http://automationpractice.com//")
assert "My Store" in driver.title
wait = WebDriverWait(driver, 10)
time.sleep(2)
driver.find_element_by_xpath("//div[@id='block_top_menu']/ul/li/a").click()
time.sleep(2)
driver.find_element_by_xpath("//ul[@id='ul_layered_category_0']/li/div/span/input").click()
