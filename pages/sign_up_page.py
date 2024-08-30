from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignUpPage(Page):
    SIGN_UP_PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Create your account in Reelly')]")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[wized='signinButtonSignup']")

    def open_sign_up(self):
        self.open_url('https://soft.reelly.io/sign-up/')

    def verify_sign_up_page_title(self):
        self.wait_for_element_appear(*self.SIGN_UP_PAGE_TITLE)
        self.verify_text('Create your account in Reelly', *self.SIGN_UP_PAGE_TITLE)

    def click_sign_in(self):
        self.wait_and_click(*self.SIGN_IN_BTN)