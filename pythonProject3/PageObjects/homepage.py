from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


button_xpath = "/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer"
input_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input"
input_pass_xpath = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input"
button_next = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[3]"
button_next2 = "/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span"
click_explore = "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/tp-yt-paper-item"
nameE = "identifier"



class HomePage:


    def __init__(self, driver):
        self.driver = driver

    @property
    def press_return_click_explore(self):
            return self.driver.find_element(by=By.XPATH, value=click_explore).click()

    def press_return_click_short(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[3]/a/tp-yt-paper-item").click()

    def press_return_click_supcriptions(self):
        return self.driver.find_element(by=By.XPATH, value=
            "/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[4]/a/tp-yt-paper-item").click()

    def press_return_click_libary(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/ytd-app/div[1]/tp-yt-app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[2]/div/ytd-guide-entry-renderer[1]/a/tp-yt-paper-item").click()

    def press_return_click(self):
        return self.driver.find_element(by=By.XPATH, value=button_xpath).click()

    def enter_return_input(self, email):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(email)
    def press_return_click_next(self):
        return self.driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys(Keys.ENTER)
    # def press_return_input(self,passw):
    #     return self.driver.find_element(by=By.XPATH, value=input_pass_xpath).send_keys(passw)
    # def press_return_click_next2(self):
    #     return self.driver.find_element(by=By.XPATH, value=button_next2).click()
    def enter_search_text(self, searchtext):
        return self.driver.find_element(by=By.NAME, value="search_query").send_keys(searchtext)

    def press_return_key_search_field(self):
        return self.driver.find_element(by=By.NAME, value='search_query').send_keys(Keys.ENTER)
