from selenium import webdriver
from selenium.webdriver.common.by import By

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
driver.implicitly_wait(10) # berfungi untuk menuggu semua baris berikutnya agar bisa jalan
# terus kenapa gak pakai wait.sleep() saja 
#karena implicitly_wait itu menuggu bukan sesudah jeda waktu ,wait.sleep()
#menuggu dia selesai misal wait 10 detik ya ditunggu hingga sudah 10 detik terus baru pindah ke baris berikutnya
#sedangkan implicitly wait itu cuma menuggu ,kalau eleemen dibawah ditemukan 2 detik kemudian
#total waktu implicityl wait ya cuma 2 detik walupun kita memasukannya 10 atau 30 detik
driver.find_element(By.XPATH, '//*[@id="APjFqb"]').send_keys('Kucing Hitam')