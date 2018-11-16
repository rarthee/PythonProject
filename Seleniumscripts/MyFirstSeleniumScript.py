from selenium import webdriver
driver=webdriver.Chrome("C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")

#To open a website
driver.get("https://google.com")

#If the page is not responding for 30 seconds then it throws an error. We can then report
#to the developer
driver.set_page_load_timeout(30)


driver.maximize_window()

##It waits for 20 seconds
driver.implicitly_wait(20)

#to capture screenshot and store it in a file
driver.get_screenshot_as_file("Google.png")

driver.quit()


