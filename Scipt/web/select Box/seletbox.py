from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/tutorSelenium/web/index.html')

#old style selet
pilih = Select(driver.find_element(By.ID,'colorSelect'))
time.sleep(2)
pilih.select_by_visible_text('Blue')

time.sleep(10)