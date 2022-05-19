#
# from selenium import webdriver
# import unittest
# import time
# from webdriver_manager.chrome import ChromeDriverManager
# button_xpath ="/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer"
# class InputPage(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Chrome(ChromeDriverManager().install())
#         cls.driver.implicitly_wait(10)
#         cls.driver.maximize_window()
#     def test_input(self):
#         self.driver.get("https://www.youtube.com/")
#         self.driver.find_element_by_link_text("Explore").click()
#         time.sleep(2)
#         self.driver.find_element_by_link_text("Shorts").click()
#         time.sleep(2)
#         self.driver.find_element_by_link_text("Subscriptions").click()
#         time.sleep(2)
#         self.driver.find_element_by_link_text("Library").click()
#         time.sleep(2)
#         self.driver.find_element_by_link_text("History").click()
#         time.sleep(2)
#         self.driver.find_element_by_xpath(button_xpath).click()
#         time.sleep(2)
#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.close()
#         cls.driver.quit()
#         print("Test Completed")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from PageObjects.youtube import HomePageYoutube
class InputPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(38)
        self.base_url = "https://www.youtube.com/"
    def testd_InputPage(self):
        driver = self.driver
        driver.get(self.base_url)
        youtube = HomePageYoutube(driver)
        youtube.click_button
        time.sleep(2)
    def tearDown(self):
        self.driver.close()
        self.driver.quit()
        print("Test Completed")

# if __name__ == "__main__":
#     unittest.main()
