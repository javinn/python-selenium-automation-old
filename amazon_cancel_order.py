# Homework 2-3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()
driver.implicitly_wait(4)
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.maximize_window()

find_more_solutions_field = driver.find_element(By.ID, "helpsearch")
sleep(2)

# ENTER is used because Go button isn't available
find_more_solutions_field.send_keys('Cancel order')
find_more_solutions_field.submit()
sleep(2)

cancel_items_header = driver.find_element(By.XPATH, '//div[@class="help-content"]/h1')

expected_header_text = 'Cancel Items or Orders'
header_text = cancel_items_header.text

assert header_text == expected_header_text, f'Error. Header text is "{header_text}" instead of "{expected_header_text}"'

# driver.quit()
