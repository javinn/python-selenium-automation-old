from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(4)

driver.get('https://www.amazon.com')

sleep(2)

input_field = driver.find_element(By.ID, 'twotabsearchtextbox')

search_icon = input_field.send_keys('Desk')
sleep(2)

search_icon = driver.find_element(By.XPATH, "//span[@id='nav-search-submit-text']/input")

search_icon.click()

search_word = driver.find_element(By.XPATH, "//span[@dir='auto' and @class='a-color-state a-text-bold']")
assert search_word.text == '"Desk"', f'Error. Searching word should be "Desk", not {search_word.text}'
