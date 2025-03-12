from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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


@when('Click on Filters button')
def click_filters(context):
    sleep(5)
    context.app.main_page.click_filters()


@when('Filter the products by "Want to sell" criteria')
def select_want_to_sell_criteria(context):
    sleep(5)
    context.app.main_page.select_want_to_sell_criteria()


@when('Click on Apply Filter button')
def click_apply_filter(context):
    sleep(5)
    context.app.main_page.click_apply_filter()


@when('Click on "Off-plan" at the left side menu')
def click_off_plan_opt(context):
    context.app.main_page.click_off_plan_opt()


@when('Off-plan page opens')
def verify_off_plan_page_title(context):
    context.app.main_page.verify_off_plan_page_title()


@when('Click on Sales status button')
def click_sales_status(context):
    sleep(5)
    context.app.main_page.click_sales_status()

@when('Drop-down list displays filter criteria')
def verify_filter_criteria(context):
    sleep(5)
    context.app.main_page.verify_filter_criteria()


@when('Filter the sales status by "Announced" criteria')
def select_announced_criteria(context):
    context.app.main_page.select_announced_criteria()


@when('Filter the sales status by "Presale(EOI)" criteria')
def select_presale_criteria(context):
    context.app.main_page.select_presale_criteria()


@when('Filter the sales status by "Out of stock" criteria')
def select_out_of_stock_criteria(context):
    context.app.main_page.select_out_of_stock_criteria()


@when('Click on "Market" at the left side menu')
def click_market_opt(context):
    context.app.main_page.click_market_opt()


@when('Market page opens')
def verify_market_page_title(context):
    context.app.main_page.verify_market_page_title()


@when('Click on "Add company" button')
def click_add_company(context):
    context.app.main_page.click_add_company()


@when('Add company page opens')
def verify_add_company_page_title(context):
    context.app.main_page.verify_add_company_page_title()


@when('Scroll down and click on "View page template" button')
def click_view_page_template(context):
    context.app.main_page.click_view_page_template()


@then('Verify all deal cards display "For sale" tag')
def verify_filter_results(context):
    sleep(5)
    context.app.main_page.verify_filter_results()


@then('Verify each deal card contains the "Announced" tag')
def verify_deal_cards(context):
    sleep(5)
    context.app.main_page.verify_deal_cards()


@then('Verify each deal card contains the "Presale(EOI)" tag')
def verify_product_cards(context):
    sleep(5)
    context.app.main_page.verify_product_cards()


@then('Verify each deal card contains the "Out of stock" tag')
def verify_project_cards(context):
    sleep(5)
    context.app.main_page.verify_project_cards()


@then('Verify the button "Send my CV" button is available')
def verify_cv_button(context):
    sleep(5)
    context.app.main_page.verify_cv_button()
