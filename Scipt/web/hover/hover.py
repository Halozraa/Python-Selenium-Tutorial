from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://www.apple.com/')
driver.implicitly_wait(10)

#cara 1
# menu = driver.find_element(By.LINK_TEXT,'"/us/shop/goto/store"')

# Hover = ActionChains(driver).move_to_element(menu)
# Hover.perform()
# time.sleep(10)

#cara 2
ActionChains(driver).move_to_element((driver.find_element(By.LINK_TEXT,'href="/us/shop/goto/store"')))
time.sleep(10)