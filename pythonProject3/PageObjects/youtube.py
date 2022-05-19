from datetime import time
import unittest
from selenium.webdriver.common.keys import Keys
button_xpath ="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer"


class HomePageYoutube:

    def __init__(self, driver):
        self.driver = driver
    def click_button(self):
        # return self.driver.find_element_by_link_text("Explore").click()
        # time.sleep(2)
        # return self.driver.find_element_by_link_text("Shorts").click()
        # time.sleep(2)
        # return self.driver.find_element_by_link_text("Subscriptions").click()
        # time.sleep(2)
        # return self.driver.find_element_by_link_text("Library").click()
        # time.sleep(2)
        # return self.driver.find_element_by_link_text("History").click()
        # time.sleep(2)
        return self.driver.find_element_by_xpath(button_xpath).click()
        # time.sleep(2)
    # def enter_search_text(self,searchtext):
    #     return self.driver.find_element_by_name("search_query").send_keys(searchtext)