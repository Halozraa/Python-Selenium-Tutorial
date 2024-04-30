from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()  #berfungsi untuk menginisialisasi sesi browser Chrome yang dapat diotomatisasi menggunakan Selenium WebDriver.

for i in range(2): #berfungi untuk melooping agar
    driver.get('https://tees.co.id/') #berfungi untuk mengarangkan ke tujuan -> () <- isi didalam ini adalh tujuannya
    driver.maximize_window() #berfungi untuk maximxze chrome lah
    time.sleep(3) #berfungi unutk menunggu 3 detik agar melanjutkan ke kodingan berikutnya


    #ini adalah contoh explisityly wait
    try:
        WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,'/html/body/div[1]')))#menunggu webdriver(driverkita, waktu tunggu).until(ini funginya untuk menunggu)(Ec = rumus .kondisi menunggunya samapi elemen yg diinvisibel muncul)
        print("Pop up muncul coy")
        driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div/div[1]').click() #mencari elemen by xpath dan diclick
        print("popup berhasil dihilangkan")
        time.sleep(2)  #berfungi unutk menunggu 2 detik agar melanjutkan ke kodingan berikutnya
    except TimeoutException: #ketika kondisi try tidak muncul ini akan di run dan akan menampilkan print
        print("Maaf popup muncul misi gagal")
        time.sleep(2)
        pass
time.sleep(10)  #berfungi unutk menunggu 10 detik agar melanjutkan ke kodingan berikutnya

