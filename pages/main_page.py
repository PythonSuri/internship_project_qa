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
    ALL_FILTER_CRITERIA = By.CSS_SELECTOR, "option[value='Announced'], option[value='Presale(EOI)'], option[value='Start if Sales'], option[value='On sale'], option[value='Out of stock']"
    ANNOUNCED_BTN = By.CSS_SELECTOR, "option[value='Announced']"
    ANNOUNCED_TAGS = (By.XPATH, "//div[@wized='projectsListing']//div[text()='Announced']")
    PRESALE_BTN = By.CSS_SELECTOR, "option[value='Presale(EOI)']"
    PRESALE_TAGS = (By.XPATH, "//div[@wized='projectsListing']//div[text()='Presale(EOI)']")
    OUTOFSTOCK_BTN = By.CSS_SELECTOR, "option[value='Out of stock']"
    OUTOFSTOCK_TAGS = (By.XPATH, "//div[@wized='projectsListing']//div[text()='Out of stock']")
    MARKET_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Market']")
    MARKET_PAGE_TITLE = (By.XPATH, "//div[@class='proparties_text_block mobile']//div[text()='Market']")
    ADD_COMPANY_BTN = (By.XPATH, "//*[@class='add-company-button w-inline-block']//div[text()='Add company']")
    ADD_COMPANY_PAGE_TITLE = (By.XPATH, "//*[@class='publish-button _1 w-button']")
    VIEW_PAGE_TEMPLATE_BTN =  (By.CSS_SELECTOR, 'a[href="https://soft.reelly.io/view-page-template?company=178"]')
    PUBLISH_MY_COMPANY_BTN = (By.CSS_SELECTOR, 'a[href="/payment/personal"]')
    SEND_MY_CV_BTN = (By.CSS_SELECTOR, 'a[href="#HR-manager"]')
    SUBSCRIPTION_PAGE_TITLE = (By.XPATH, "//*[@class='pricing-header']")
    SETTINGS_BTN = (By.XPATH, "//*[@class='w-layout-grid menu_grid']//div[text()='Settings']")
    VERIFICATION_BTN = (By.XPATH, "//*[@class='page-setting-block w-inline-block']//div[text()='Verification']")
    VERIFICATION_PAGE_TITLE = (By.XPATH, "//*[@class='verify-step-block']//div[text()='Upload your photo']")
    UPLOAD_IMG_BTN = (By.XPATH, "//*[@class='upload-button-2 w-embed']")
    NEXT_STEP_BTN = (By.XPATH, "//a[@wized='nextButtonStep0']//div[text()='Next step ->']")


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

    def verify_deal_cards(self):
        self.wait_for_element_appear(*self.ANNOUNCED_TAGS)
        self.verify_text('Announced',*self.ANNOUNCED_TAGS)

    def select_presale_criteria(self):
        sleep(2)
        self.wait_for_element_appear(*self.PRESALE_BTN)
        self.wait_and_click(*self.PRESALE_BTN)

    def verify_product_cards(self):
        self.wait_for_element_appear(*self.PRESALE_TAGS)
        self.verify_text('Presale(EOI)', *self.PRESALE_TAGS)

    def select_out_of_stock_criteria(self):
        sleep(2)
        self.wait_for_element_appear(*self.OUTOFSTOCK_BTN)
        self.wait_and_click(*self.OUTOFSTOCK_BTN)

    def verify_project_cards(self):
        self.wait_for_element_appear(*self.OUTOFSTOCK_TAGS)
        self.verify_text('Out of stock', *self.OUTOFSTOCK_TAGS)

    def click_market_opt(self):
        sleep(2)
        self.wait_and_click(*self.MARKET_BTN)

    def verify_market_page_title(self):
        self.wait_for_element_appear(*self.MARKET_PAGE_TITLE)
        self.verify_text('Market', *self.MARKET_PAGE_TITLE)

    def click_add_company(self):
        sleep(2)
        self.wait_and_click(*self.ADD_COMPANY_BTN)

    def verify_add_company_page_title(self):
        self.wait_for_element_appear(*self.ADD_COMPANY_PAGE_TITLE)
        self.verify_text('Publish my company', *self.ADD_COMPANY_PAGE_TITLE)

    def verify_subscription_page_title(self):
        sleep(2)
        self.wait_for_element_appear(*self.SUBSCRIPTION_PAGE_TITLE)
        self.verify_text('Find your plan', *self.SUBSCRIPTION_PAGE_TITLE)

    def click_view_page_template(self):
        sleep(5)
        self.wait_for_element_appear(*self.VIEW_PAGE_TEMPLATE_BTN)
        self.wait_and_click(*self.VIEW_PAGE_TEMPLATE_BTN)

    def click_publish_my_company(self):
        sleep(5)
        self.wait_for_element_appear(*self.PUBLISH_MY_COMPANY_BTN)
        self.wait_and_click(*self.PUBLISH_MY_COMPANY_BTN)

    def verify_cv_button(self):
        sleep(3)
        self.wait_for_element_appear(*self.SEND_MY_CV_BTN)
        self.wait_and_click(*self.SEND_MY_CV_BTN)

    def click_settings_opt(self):
        sleep(5)
        self.wait_and_click(*self.SETTINGS_BTN)

    def click_verification_opt(self):
        sleep(5)
        self.wait_and_click(*self.VERIFICATION_BTN)

    def verify_verification_page_title(self):
        self.wait_for_element_appear(*self.VERIFICATION_PAGE_TITLE)
        self.verify_text('Upload your photo', *self.VERIFICATION_PAGE_TITLE)

    def verify_upload_image_button(self):
        sleep(3)
        self.wait_for_element_appear(*self.UPLOAD_IMG_BTN)
        self.verify_text('Upload image', *self.UPLOAD_IMG_BTN)

    def verify_next_step_button(self):
        sleep(3)
        self.wait_for_element_appear(*self.NEXT_STEP_BTN)
        self.verify_text('Next step ->', *self.NEXT_STEP_BTN)

    def verify_sales_status_button(self):
        sleep(3)
        self.wait_for_element_appear(*self.SALES_STATUS_BTN)
        self.wait_and_click(*self.SALES_STATUS_BTN)