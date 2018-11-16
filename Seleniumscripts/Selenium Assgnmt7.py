#http://qatechhub.com/selenium-assignment-6/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://jqueryui.com/droppable/")
driver.maximize_window()
actionChains = ActionChains(driver)
#source=driver.find_element_by_xpath("div[@id='draggable']").click()
#target=driver.find_element_by_xpath("div[@id='droppable']").click()
source=getattr()
actionChains.drag_and_drop(source, target).perform()

