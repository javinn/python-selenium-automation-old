# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# # init driver
#
# driver = webdriver.Chrome()
# # chromedriver.exe copied to c:\bin and this added to system variable Path
# driver.maximize_window()

# open the url
# driver.get('https://www.google.com/')
#
# search = driver.find_element(By.NAME, 'q')
# search.clear()
# search.send_keys('Dress')
#
# # wait for 4 sec
# sleep(4)
#
# # click search
# driver.find_element(By.NAME, 'btnK').click()
#
# # verify
# assert 'Dress' in driver.find_element(By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]").text
# assert 'Dress' in driver.find_element(By.XPATH, "//div[@class='g']").text
#
# driver.quit()

def spin_words(sentence):
    g_in = 0
    l_in = 0
    result = ''
    current_word = ''
    
    while g_in < len(sentence):
        while sentence[g_in+l_in] != ' ':


        g_in += 1

        return None
