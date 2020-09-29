from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.amazon.com/gp/help/customer/display.html')
driver.maximize_window()

find_more_solutions_field = driver.find_element(By.ID, "helpsearch")

# ENTER is used because Go button isn't available
find_more_solutions_field.send_keys('Cancel order', Keys.ENTER)
