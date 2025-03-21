import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger


## Command to run tests with Allure & Behave:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/target_search.feature
## Command to show allure results:
# allure serve test_results/


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    ### BROWSERS WITH DRIVERS: provide path to the driver file ###
    # service = Service(executable_path='/Users/svetlanalevinsohn/careerist/19-python-selenium-automation/geckodriver')

    #############################################################
    ### Chrome ###
    # driver_path = './chromedriver'
    # service = Service(driver_path)
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)

    ### HEADLESS MODE CHROME ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ##############################################################
    ### Firefox ###
    # driver_path = GeckoDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Firefox(service=service)

    ### HEADLESS MODE Firefox####
    # options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path='/Users/surayya/Downloads/internship_project_qa/geckodriver')
    # context.driver = webdriver.Firefox(service=service, options=options)

    ############################################################
    ### SAFARI ###
    # context.driver = webdriver.Safari()


    # BROWSERSTACK ##
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # Select a browser and operating system to test: https://www.browserstack.com/docs/automate/capabilities
    # bs_user = 'suriaziz_cDPzFk'
    # bs_key = 'CNhLSuXeLXzsFFjLBuqf'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Monterey",
    #     'browserName': "chrome",
    #     "sessionName": "scenario_name"
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)


    ## Mobile Emulation CHROME##
    # chrome_options = webdriver.ChromeOptions()
    # mobile_emulation = {"deviceName": "Samsung Galaxy S20 Ultra"}
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service, options=chrome_options)


    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)


def before_scenario(context, scenario_name):
    print('\nStarted scenario: ', scenario_name)
    logger.info(f'\nStarted scenario: {scenario_name}')
    browser_init(context, scenario_name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
