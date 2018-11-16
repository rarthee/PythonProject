#http://qatechhub.com/selenium-assignment-3/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://flipkart.com")
driver.maximize_window()

#To count number of links on facebook page
#Links start with 'a' tag

for a in driver.find_elements_by_xpath('.//a'):
    print(a.get_attribute('href'))
