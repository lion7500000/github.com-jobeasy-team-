from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    TEXT_IN_ITEMS = (By.CSS_SELECTOR, "div a.description")

    def __init__ (self, driver):
        self.driver = driver
        self.base_url = 'https://honorlock.instructure.com/login/canvas'
        self.wait = WebDriverWait(self.driver,15)
        self.action = ActionChains(self.driver)

    def input_text (self, text, *locator):
        serch_icon = self.driver.find_element (*locator)
        serch_icon.clear()
        serch_icon.send_keys(text)

    def click (self, *locator):
        self.driver.find_element(*locator).click()

    def serch_items (self, *locator):
        self.driver.find_element(*locator)

    def verify_text (self,expected_text,*locator):
        actual_text = self.driver.find_element(*locator).text
        print (actual_text)
        assert expected_text in actual_text, f'Expected text {expected_text}, but got {actual_text}'

