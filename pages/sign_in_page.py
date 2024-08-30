from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignInPage(Page):
    SIGN_IN_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Sign in or create new account')]")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[wized='loginButton']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "[wized='emailInput'][placeholder='Email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[wized='passwordInput'][placeholder='Password']")
    EMAIL = '********'  # => VALID EMAIL
    # USE INVALID EMAIL for Negative Scenario
    PASSWORD = '********'  # => VALID PASSWORD
    # USE INVALID PASSWORD for Negative Scenario
    USER_LOGGED_PAGE = (By.CSS_SELECTOR, "[class='page-title off_plan']")

    def open_sign_in(self):
        self.open_url('https://soft.reelly.io/sign-in/')

    def verify_sign_in_page_title(self):
        self.wait_for_element_appear(*self.SIGN_IN_PAGE_TITLE)
        self.verify_text('Sign in or create new account', *self.SIGN_IN_PAGE_TITLE)

    def click_continue(self):
        self.wait_and_click(*self.CONTINUE_BTN)

    def enter_credentials(self):
        self.input_text(self.EMAIL, *self.EMAIL_FIELD)
        self.input_text(self.PASSWORD, *self.PASSWORD_FIELD)

    def verify_logged_user(self):
        self.wait_for_element_appear(*self.USER_LOGGED_PAGE)
        self.verify_text('Total projects', *self.USER_LOGGED_PAGE)