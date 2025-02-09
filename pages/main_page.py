from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class MainPage(Page):
    HEADER_TITLE = (By.XPATH, "//div[contains(text(),'Total projects')]")
    # SECONDARY_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Secondary']")  ## web version
    SECONDARY_BTN = (By.CSS_SELECTOR, "a[wized='mobileTabGame']")  ## mobile version
    FILTERS_BTN = (By.CSS_SELECTOR, "[class='filter-button']")
    WANT_TO_SELL_BTN = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAGS = (By.XPATH, "//*[@class='listing-card']//div[text()='For sale']")

    def verify_header_title(self):
        self.wait_for_element_appear(*self.HEADER_TITLE)
        self.verify_text('Total projects', *self.HEADER_TITLE)

    def click_secondary_opt(self):
        sleep(5)
        self.wait_and_click(*self.SECONDARY_BTN)

    def click_filters(self):
        sleep(5)
        self.wait_and_click(*self.FILTERS_BTN)

    def select_want_to_sell_criteria(self):
        self.wait_and_click(*self.WANT_TO_SELL_BTN)

    def click_apply_filter(self):
        self.wait_and_click(*self.APPLY_FILTER_BTN)

    def verify_filter_results(self):
        self.wait_for_element_appear(*self.FOR_SALE_TAGS)
        self.verify_text('For sale', *self.FOR_SALE_TAGS)
