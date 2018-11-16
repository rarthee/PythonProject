import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.keys import Keys
import time

class PythonOrgSearchChrome(unittest.TestCase):

#Set up  is a method that is used to fill in prerequisites like browser,website to test etc
    def setUp(self):
        self.driver=webdriver.Chrome("C:\\Users\\Sahana Rangarajan\\PycharmProjects\\Pythontutorials\\Seleniumscripts\\Chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://www.phptravels.net/")
        assert "PHPTRAVELS" in self.driver.title
        wait = WebDriverWait(self.driver, 10)


    def test_case01(self):
        self.driver.find_element_by_xpath("//*[@id='s2id_autogen8']").click()
        wait = WebDriverWait(self.driver, 10)
     #  text_area= self.driver.find_element_by_xpath("//*[@id='s2id_autogen8']")
     #  wait = WebDriverWait(driver, 10)
     #  text_area.send_keys("Indiana, Unites States")
     #  text_area.send_keys(Keys.RETURN)
        self.driver.find_element_by_xpath("//input[@placeholder='Check in']").send_keys("07/11/2017")
        self.driver.find_element_by_xpath("//input[@placeholder='Check out']").send_keys("09/11/2018")
        self.driver.find_element_by_id("travellersInput").click()
        self.driver.find_element_by_id("travellersInput").send_keys("2 Adult 2 Child")
        self.driver.find_element_by_class_name("//button[@class='btn btn-lg btn-block btn-primary pfb0 loader']")

#def tearDown(self):
    #    Close the browser.
     #   self.driver.close()









