from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


class MainPage(Page):
    HEADER_TITLE = (By.XPATH, "//div[contains(text(),'Total projects')]")
    SECONDARY_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Secondary']")  ## web version
    # SECONDARY_BTN = (By.CSS_SELECTOR, "a[wized='mobileTabGame']")  ## mobile version
    FILTERS_BTN = (By.CSS_SELECTOR, "[class='filter-button']")
    WANT_TO_SELL_BTN = (By.CSS_SELECTOR, '[wized="ListingTypeSell"]')
    APPLY_FILTER_BTN = (By.CSS_SELECTOR, 'a[wized="applyFilterButtonMLS"]')
    FOR_SALE_TAGS = (By.XPATH, "//*[@class='listing-card']//div[text()='For sale']")
    OFF_PLAN_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Off-plan']")
    OFF_PLAN_PAGE_TITLE = (By.XPATH, "//div[contains(text(),'Total projects')]")
    SALES_STATUS_BTN = (By.CSS_SELECTOR, '[wized="saleStatusFilter"]')
    ANNOUNCED_BTN = By.CSS_SELECTOR, "option[value='Announced']"
    ANNOUNCED_TAGS = (By.XPATH, "//div[@wized='projectsListing']//div[text()='Announced']")


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

    def click_off_plan_opt(self):
        sleep(2)
        self.wait_and_click(*self.OFF_PLAN_BTN)

    def verify_off_plan_page_title(self):
        self.wait_for_element_appear(*self.OFF_PLAN_PAGE_TITLE)
        self.verify_text('Total projects', *self.OFF_PLAN_PAGE_TITLE)

    def click_sales_status(self):
        sleep(2)
        self.wait_and_click(*self.SALES_STATUS_BTN)

    def select_announced_criteria(self):
        sleep(2)
        self.wait_for_element_appear(*self.ANNOUNCED_BTN)
        self.wait_and_click(*self.ANNOUNCED_BTN)
    # def select_announced_criteria(self):
    #     sleep(5)
    #     self.wait_and_click(*self.ANNOUNCED_BTN)

    def verify_deal_cards(self):
        self.wait_for_element_appear(*self.ANNOUNCED_TAGS)
        self.verify_text('Announced', *self.ANNOUNCED_TAGS)