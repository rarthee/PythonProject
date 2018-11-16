#http://qatechhub.com/selenium-assignment-5 and 6/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://www.snapdeal.com")
driver.maximize_window()


driver.find_element_by_xpath("//div[@class='topBar  top-bar-homepage  top-freeze-reference-point']/div/div[3]/div[3]/div/span").click()
driver.find_element_by_xpath("//*[@id='sdHeader']/div[4]/div[2]/div/div[3]/div[3]/div/div/div[2]/div[2]/span[2]/a").click()
#driver.find_element_by_xpath("//div[@id='signin_box']/div/div/div[4]/form/div/input").click()

#driver.find_elements_by_class_name("col-xs-24 clickOnceOnly").click()
#driver.find_elements_by_id("'userName'][2]").click()
