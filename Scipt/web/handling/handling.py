from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

# 74, 245
# while True :
#     print(pyautogui.position())
#     time.sleep(2)
driver = webdriver.Chrome()  #berfungsi untuk menginisialisasi sesi browser Chrome yang dapat diotomatisasi menggunakan Selenium WebDriver.
driver.get('file:///C:/Users/Admin/Desktop/LEARN PROGRAMMER/3.Mini Project/CREATE PROGRAM WITH PYTHON/tutorSelenium/web/index.html') #berfungi untuk menjalkan file html(Tiap org beda beda lokasiny ya)
time.sleep(2)
driver.maximize_window() #berfungi untuk maximxze chrome lah
time.sleep(2)


# cara satu kalau alertnya/notif cuma ada accpect/ok doang
pyautogui.click(85,255) # unutk mengarahkan mouse kita secara otomatis ke posisi (x,y) dengan pyautogui dan mengkliknya
time.sleep(20)
driver.switch_to.alert.accept() #untuk menerima  alert ok
time.sleep(20)

#cara 2 kalau alertnya ada tulisan ok or no
pyautogui.click(158,255) 
time.sleep(20)
#kalian bisa pilih mau menggunakan yang mana satu saja

driver.switch_to.alert.dismiss() # untuk menolak alert/notif
driver.switch_to.alert.accept() #untuk menerima alert/notif
time.sleep(20)