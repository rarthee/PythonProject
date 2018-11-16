#http://qatechhub.com/selenium-assignment-3/
from selenium import webdriver
import urllib
import re
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://flipkart.com")
driver.maximize_window()

#for the popup login page in flipkart

driver.implicitly_wait(3)
driver.find_element_by_class_name('fk-modal-visible').click()

driver.find_element_by_xpath("/html/body/div[2]/div/div/button").click()
