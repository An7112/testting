from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time
from PageObjects.homepage import HomePage
class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(38)
        self.base_url = "https://www.youtube.com/"
    def testd_google_search(self):
        driver = self.driver
        driver.get(self.base_url)
        homepage = HomePage(driver)
        homepage.press_return_click_explore
        time.sleep(2)
        homepage.press_return_click_short()
        time.sleep(2)
        homepage.press_return_click_supcriptions()
        time.sleep(2)
        homepage.press_return_click_libary()
        time.sleep(2)
        homepage.enter_search_text("An")
        homepage.press_return_key_search_field()
        time.sleep(2)
        homepage.press_return_click()
        time.sleep(2)
        homepage.enter_return_input("thanhan7112@gmail.com")
        time.sleep(2)
        homepage.press_return_click_next()
        time.sleep(2)
        # homepage.press_return_input("0201172001An")
        # homepage.press_return_click_next2()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()