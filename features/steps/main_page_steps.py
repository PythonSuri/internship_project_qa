from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from selenium.webdriver.common.by import By

from time import sleep


@when('Main page opens')
def verify_header_title(context):
    context.app.main_page.verify_header_title()


@when('Click on “Secondary” option at the left side menu')
def click_secondary_opt(context):
    context.app.main_page.click_secondary_opt()


@when('Click on Filters')
def click_filters(context):
    context.app.main_page.click_filters()


@when('Filter the products by "Want to sell"')
def select_want_to_sell_criteria(context):
    context.app.main_page.select_want_to_sell_criteria()


@when('Click on Apply Filter')
def click_apply_filter(context):
    context.app.main_page.click_apply_filter()


@then('Verify all cards have "For sale" tag')
def verify_filter_results(context):
    context.app.main_page.verify_filter_results()
