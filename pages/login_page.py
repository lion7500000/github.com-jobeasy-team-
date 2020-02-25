from pages.base_page import Page
from selenium.webdriver.common.by import By

class LoginPage(Page):

    Login_page = (By.CSS_SELECTOR, "input#pseudonym_session_unique_id")
    Password_page = (By.CSS_SELECTOR, "input#pseudonym_session_password")
    Login_button = (By.CSS_SELECTOR, "button.Button--login")
    Error_text = (By.CSS_SELECTOR, "li.ic-flash-error")

    def open_page (self):
        self.driver.get(self.base_url)

    def input_login(self,text):
        self.input_text(text,*self.Login_page)

    def input_password(self,text):
        self.input_text(text, *self.Password_page)

    def click_login_button(self):
        self.click(*self.Login_button)

    def verify_error (self,expected_text):
        self.verify_text(expected_text,*self.Error_text)
