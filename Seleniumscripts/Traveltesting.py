import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.maximize_window()

driver.get("https://www.phptravels.net/")
assert "PHPTR" in driver.title
wait = WebDriverWait(driver, 10)
driver.find_element_by_xpath("//div[@class='col-md-12']/ul/li/a/span").click()
#time.sleep(2)
driver.find_element_by_xpath("//div[@id='s2id_location_from']/a/span").click()
time.sleep(2)
#driver.find_elements_by_xpath(
#    "//div[@class='select2-drop select2-display-none select2-with-searchbox select2-drop-active']/div/input")[
#    0].send_keys("India", Keys.ENTER)
time.sleep(2)
#driver.find_elements_by_xpath(
#            "//li[@class='select2-results-dept-1 select2-result select2-result-selectable select2-highlighted']/div")[
#            1].click()
time.sleep(2)
driver.find_element_by_xpath(
"//div[@class='select2-drop select2-display-none select2-with-searchbox select2-drop-active']/div/input").send_keys("India", Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("//div[@id='s2id_location_from']/a/span").click()

driver.find_element_by_xpath("//li[@class='select2-results-dept-1 select2-result select2-result-selectable select2-highlighted']/div/span").click()



















