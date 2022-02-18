from behave import *

import os
from selenium import webdriver

def open_browser(test_name):
    caps = {
        'browserName': 'chrome',
        'browserVersion': 'latest',
        'platformName': 'Windows 10',
        'sauce:options': {
            'name': test_name
        }
    }

    username = os.environ['SAUCE_USERNAME']
    access_key = os.environ['SAUCE_ACCESS_KEY']

    sauce_url = 'http://{}:{}@ondemand.saucelabs.com/wd/hub/'.format(username, access_key)

    return webdriver.Remote(sauce_url, desired_capabilities=caps)


@given('we visit the login page')
def step_impl(context):
    test_name = str(context.feature)
    context.browser = open_browser(test_name)
    context.browser.get('https://www.saucedemo.com')

@given('we visit the inventory page')
def step_impl(context):
    test_name = str(context.feature)
    context.browser = open_browser(test_name)
    context.browser.get('https://www.saucedemo.com/v1/inventory.html')

@when('we login as a standard user')
def step_impl(context):
    context.browser.find_element_by_id('user-name').send_keys('standard_user')
    context.browser.find_element_by_id('password').send_keys('secret_sauce')
    context.browser.find_element_by_id('login-button').click()

@when('we login as an invalid user')
def step_impl(context):
    context.browser.find_element_by_id('user-name').send_keys('bad')
    context.browser.find_element_by_id('password').send_keys('bad')
    context.browser.find_element_by_id('login-button').click()

@when('we add one item to the cart')
def step_impl(context):
    context.browser.find_element_by_css_selector('.btn_primary').click()

@when('we remove one item from the cart')
def step_impl(context):
    context.browser.find_element_by_css_selector('.btn_secondary').click()

@then('we should see the shopping cart')
def step_impl(context):
    # NOTE: BAD PRACTICE to use try/except/finally instead of before/after hooks in environment.py
    try:
        assert context.browser.find_element_by_css_selector('.shopping_cart_container').is_displayed()
    finally:
        context.browser.quit()

@then('we should see the error icon')
def step_impl(context):
    # NOTE: BAD PRACTICE to use try/except/finally instead of before/after hooks in environment.py
    try:
        assert context.browser.find_element_by_css_selector('.error-button').is_displayed()
    finally:
        context.browser.quit()

@then('we should see an item in the cart')
def step_impl(context):
    # NOTE: BAD PRACTICE to use try/except/finally instead of before/after hooks in environment.py
    try:
        assert context.browser.find_element_by_css_selector('.shopping_cart_badge').is_displayed()
    finally:
        context.browser.quit()

@then('we should not see an item in the cart')
def step_impl(context):
    # NOTE: BAD PRACTICE to use try/except/finally instead of before/after hooks in environment.py
    try:
        assert len(context.browser.find_elements_by_css_selector('.shopping_cart_badge')) == 0
    finally:
        context.browser.quit()