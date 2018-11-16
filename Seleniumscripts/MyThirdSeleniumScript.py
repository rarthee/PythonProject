from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")

#To find any actions we can check using 'driver.'


#To open a website
driver.get("https://www.facebook.com")

#If the page is not responding for 30 seconds then it throws an error. We can then report
#to the developer
driver.set_page_load_timeout(30)

# Assert is used to test a condition. Here we are checking if the word 'facebook' is
#present in the title or not.

print(driver.title)
assert "Facebook" in driver.title

driver.maximize_window()

##It waits for 20 seconds
driver.implicitly_wait(20)

#to capture screenshot and store it in a file
driver.get_screenshot_as_file("./Screenshots/Facebook.png")

driver.find_element_by_id("email").send_keys("Selenium Webdriver")
driver.find_element_by_name("pass").send_keys("Python")
driver.find_element_by_id("loginbutton").click()

driver.get_screenshot_as_file("./Screenshots/Facebook1.png")
driver.quit()


