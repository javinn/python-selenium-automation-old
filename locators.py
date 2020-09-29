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

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


my_driver = webdriver.Chrome()

my_driver.implicitly_wait(4)

my_driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')

sleep(2)

my_driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]').click()

sleep(2)

my_driver.find_element(By.ID, "auth-fpp-link-bottom").click()

sleep(2)

my_driver.quit()