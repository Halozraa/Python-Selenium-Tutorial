from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


driver = webdriver.Chrome()  #berfungsi untuk menginisialisasi sesi browser Chrome yang dapat diotomatisasi menggunakan Selenium WebDriver.
driver.get('file:///C:/Users/Admin/Desktop/LEARN PROGRAMMER/3.Mini Project/CREATE PROGRAM WITH PYTHON/tutorSelenium/web/index.html') #berfungi untuk menjalkan file html(Tiap org beda beda lokasiny ya)
time.sleep(2)
driver.maximize_window() #berfungi untuk maximxze chrome lah
time.sleep(2)

pyautogui.click(85,255) # unutk mengarahkan mouse kita secara otomatis ke posisi (x,y) dengan pyautogui dan mengkliknya

#ini adalah contoh explisityly wait
try :
    WebDriverWait(driver,20).until(EC.alert_is_present()) #menunggu webdriver(driverkita, waktu tunggu).until(ini funginya untuk menunggu)(Ec = rumus .kondisi menunggunya samapi apa )
    driver.switch_to.alert.accept() #untuk menerima  alert ok
    print("Alert sudah Diclick")
except TimeoutException:
    print("Alert tidak ditemukan")
    pass
time.sleep(20)