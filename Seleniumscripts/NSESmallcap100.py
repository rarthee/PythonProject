from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

mylistfromdt=['02-01-2017','01-12-2017']
mylisttodt  =['02-11-2017','03-11-2018']

mylistselindx= ["NIFTY 50","NIFTY MIDCAP 100","NIFTY SMALLCAP 100"]

driver=webdriver.Chrome("C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
SCROLL_PAUSE_TIME = 0.5

driver.get("https://www.nseindia.com")
driver.maximize_window()

driver.get("https://nseindia.com/products/content/equities/indices/indices.htm")

wait = WebDriverWait(driver, 10)

#To click historical data
driver.find_element_by_xpath("//*[@id='wrapper_btm']/div[1]/div[1]/div/div[3]/h3/span").click()




#count for each year range for a single selected index
count=0
while (count<2):
    print("count is ",count)
    # To click P/E,P/B & Div
    driver.get("https://nseindia.com/products/content/equities/indices/historical_pepb.htm")
    #driver.find_element_by_id("IndexName").clear()
    myselect=Select(driver.find_element_by_id("IndexName"))
    myselect.select_by_value(mylistselindx[2])
    driver.find_element_by_id("fromDate").clear()
    driver.find_element_by_id("fromDate").send_keys(mylistfromdt[count])
    driver.find_element_by_id("toDate").clear()
    driver.find_element_by_id("toDate").send_keys(mylisttodt[count])
    driver.find_element_by_id("yield4").click()
    # driver.find_element_by_id("get").clear()
    driver.find_element_by_id("get").click()

    #Below code helps in scrolling down dynamically
    # Get scroll height
    last_height=0
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
    # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #Select the download button
    wait = WebDriverWait(driver, 10)
    driver.find_element_by_xpath("//*[@id='replacetext']/table/tbody[2]/tr/td/a").click()
    count = count + 1


print("end of loop")










