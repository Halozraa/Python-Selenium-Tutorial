from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get('https://jqueryui.com/datepicker/')

driver.switch_to.frame(driver.find_element(By.XPATH,'//*[@id="content"]/iframe'))

# driver.find_element(By.ID,'datepicker').click()
# driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[2]/td[6]/a').click()
driver.find_element(By.ID,'datepicker').send_keys('04/12/2024')

time.sleep(2)