import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://fb.com//")
driver.maximize_window()
time.sleep(2)
print(driver.current_url)
if driver.current_url == "https://www.facebook.com/":
    print("The url is correct")
else:
    print("The url is incorrect")

#assert "Create an account" in driver.find_elements(str)

time.sleep(2)

#driver.quit()
