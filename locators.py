# Homework 2-2

"""

(By.XPATH, '//i[@aria-label="Amazon"]')                     - Amazon Logo
(By.ID, "continue")                                         - Continue button
(By.XPATH, '//span[@class="a-expander-prompt"]')            - Need help link
(By.ID, "auth-fpp-link-bottom")                             - Forgot your password link
(By.ID, "ap-other-signin-issues-link")                      - Other issues with Sign-In link
(By.ID, "createAccountSubmit")                              - Create your Amazon account button
(By.LINK_TEXT, 'Conditions of Use')                         - Conditions of use link
(By.PARTIAL_LINK_TEXT, 'Privacy Not')                       - Privacy Notice link


"""
# Homework 3-1

"""

(By.CSS_SELECTOR, 'i.a-icon-logo')                                                      - Amazon Logo
(By.CSS_SELECTOR, 'h1.a-spacing-small')                                                 - Create account
(By.CSS_SELECTOR, 'input#ap_customer_name')                                             - Your name
(By.CSS_SELECTOR, 'input#ap_email')                                                     - Email
(By.CSS_SELECTOR, 'input#ap_password')                                                  - Password
(By.CSS_SELECTOR, 'div.auth-inlined-information-message div.a-alert-content')           - Password restriction





"""




# Script for testing purpose
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys



my_driver = webdriver.Chrome()

my_driver.implicitly_wait(4)

my_driver.get('https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26ref_%3Dnav_custrec_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(2)

password_restriction = my_driver.find_element(By.CSS_SELECTOR, 'div.auth-inlined-information-message div.a-alert-content')

sleep(2)

# password_restriction.send_keys('JavInn', Keys.ENTER)
expected_text = 'Passwords must be at least'

assert expected_text in password_restriction.text, f'Error! Expected \'{expected_text}\' but got \'{password_restriction.text}\''

sleep(4)


my_driver.quit()