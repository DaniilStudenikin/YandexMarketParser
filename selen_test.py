import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.google.com')

# search = browser.find_element('q')
# search.send_keys("google search through python")
# search.send_keys(Keys.RETURN)  # hit return after you enter search text
time.sleep(5)  # sleep for 5 seconds so you can see the results
browser.get("https://market.yandex.ru/")
time.sleep(5)
browser.quit()
