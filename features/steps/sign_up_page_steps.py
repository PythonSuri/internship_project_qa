from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

from selenium.webdriver.common.by import By
from time import sleep


@given('Open Reelly sign up page')
def open_sign_up(context):
    context.app.sign_up_page.open_sign_up()


@when('Click on Sign in')
def click_sign_in(context):
    context.app.sign_up_page.click_sign_in()


@then('Verify Sign up page title')
def verify_sign_up_page_title(context):
    context.app.sign_up_page.verify_sign_up_page_title()