from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then

from selenium.webdriver.common.by import By
from time import sleep


@given('Open Reelly sign in page')
def open_sign_in(context):
    context.app.sign_in_page.open_sign_in()


@when('Enter a valid email and password combination')
def enter_credentials(context):
    context.app.sign_in_page.enter_credentials()


@when('Click on Continue')
def click_continue(context):
    context.app.sign_in_page.click_continue()


@when('Sign in page opens')
def verify_sign_in_page_title(context):
    context.app.sign_in_page.verify_sign_in_page_title()


@then('Verify user is logged in')
def verify_logged_user(context):
    context.app.sign_in_page.verify_logged_user()