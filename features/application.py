from pages.login_page import LoginPage


class Application:

    def __init__(self,driver):
        self.driver = driver
        self.login_page = LoginPage(self.driver)