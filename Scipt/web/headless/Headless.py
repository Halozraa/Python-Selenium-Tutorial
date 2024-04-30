import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get('https://m.kuku.lu/new.php')

driver.find_element(By.ID,'sendmail_to').send_keys('boltzzero12@gmail.com')
driver.find_element(By.ID,'sendmail_subject').send_keys('Promo menarik Bagi anda yang')
driver.find_element(By.ID,'sendmail_content').send_keys("Apa anda mau Mobil tentukan dipromo megah kita")
time.sleep(5)
driver.find_element(By.ID,'area_sendbutton').click()
time.sleep(2)
print("click captha berhasil")
driver.find_element(By.ID,'area-confirm-dialog-button-ok').click()
driver.find_element(By.ID,'area-confirm-dialog-button-ok').click()


# time.sleep(20)
# https://github.com/2captcha/2captcha-python

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from twocaptcha import TwoCaptcha

api_key = os.getenv('APIKEY_2CAPTCHA', '9239bfce02bfef2953b85f0a083cc355')

solver = TwoCaptcha(api_key)

try:
    result = solver.recaptcha(
        sitekey='6LfD3PIbAAAAAJs_eEHvoOl75_83eXSqpPSRFJ_u',
        url='https://2captcha.com/demo/recaptcha-v2')

except Exception as e:
    sys.exit(e)

else:
    sys.exit('solved: ' + str(result))