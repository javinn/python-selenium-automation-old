#  Homework 2-4

from selenium.webdriver.common.by import By
from behave import given, when, then

RETURNS_AND_ORDERS = (By.ID, "nav-orders")
SIGNIN_HEADER = (By.XPATH, '//h1[@class="a-spacing-small"]')


@given('Open {webpage}')
def open_wbepage(context, webpage):
    context.driver.get(webpage)


@when('Click on Returns & Orders')
def click_on_returns_and_orders(context):
    context.driver.find_element(*RETURNS_AND_ORDERS).click()


@then('Sign-in page opens')
def verify_sign_in_field(context):
    assert 'Sign-In' in context.driver.find_element(*SIGNIN_HEADER).text, 'Error!!! Sign-in page not found'



