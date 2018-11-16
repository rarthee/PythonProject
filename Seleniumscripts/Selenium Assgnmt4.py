#http://qatechhub.com/selenium-assignment-4/
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome(
            "C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
driver.get("http://ebay.com")
driver.maximize_window()


driver.find_element_by_xpath("//div[@id='gh-ac-box2']/input").click()
driver.find_element_by_xpath("//div[@id='gh-ac-box2']/input").send_keys("Apple Watches")

driver.find_element_by_id("gh-shop-a").click()
#driver.find_elements_by_xpath('/html/body/header/table/tbody/tr/td[2]/div/div/table/tbody/tr/td[2]/ul[1]/li[3]/a').click()
driver.find_element_by_id("gh-btn").click()

for a in driver.find_elements_by_class_name('s-item__title'):
    print(a.text)


