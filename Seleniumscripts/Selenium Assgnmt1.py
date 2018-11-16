import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://qatechhub.com//")
driver.maximize_window()
time.sleep(2)
assert "QA Automation Tools Trainings and Tutorials | QA Tech Hub" in driver.title
driver.get("https://www.facebook.com")
time.sleep(2)
driver.back()
driver.quit()
