from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time

driver = webdriver.Chrome() #berfungsi untuk menginisialisasi sesi browser Chrome yang dapat diotomatisasi menggunakan Selenium WebDriver.

driver.get("https://www.google.com/") #berfungsi untuk membuka halaman web google dan .get berfungi untuk mengarahkan ("tujuan") <- () adalah tujuan get mengarahkannya
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Kucing Hitam') #untuk mencari elemen dalam xpat dan send keys untuk memasukan teks
time.sleep(2) # ini adalah baris jeda waktu
pyautogui.press('enter') #ini berfungi untuk menekan enter secara otomatis
time.sleep(2) # ini adalah baris jeda waktu
driver.maximize_window()# ini seperti namanya berfungsi untuk maximize atau untuk memperbesar secara otomatis
time.sleep(2) # ini adalah baris jeda waktu
driver.minimize_window() # ini seperti namanya berfungi untuk menimize secara otomatis windows
time.sleep(2) # ini adalah baris jeda waktu