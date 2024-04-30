from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui

#yg dibawan inin untuk menggunakan explisty wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

def  upload():
    title = "Upload Auto"
    text = "  1.Upload cara 1\n  2.upload cara 2\nmasukan pilihan anda :"
    display = int(pyautogui.prompt(text,title))

    driver = webdriver.Chrome()  #berfungsi untuk menginisialisasi sesi browser Chrome yang dapat diotomatisasi menggunakan Selenium WebDriver.
    driver.implicitly_wait(10) #untuk menuggu setiap 10 detik tiap baris agar menemukan tujuannya
    driver.get('https://filebin.net/') 
    #pilih salah satu aja meng
    while True :
        try :
            if display == 1:
                #cara 1 upload file harus ada inputnya di inspect elemennya bos
                driver.find_element(By.ID,'fileField').send_keys('C:/Users/Admin/Desktop/LEARN PROGRAMMER/3.Mini Project/CREATE PROGRAM WITH PYTHON/tutorSelenium/web/index.html')
                time.sleep(10)

            elif display == 2:
                #cara 2 upload file bersama pyautogui kalau gak ada inputnya
                pyautogui.click(167,320) #kenpa gk pake find elemen bang karena gw link xpath nya salah mulu cok
                time.sleep(3)
                pyautogui.write('C:\\Users\Admin\Desktop\LEARN PROGRAMMER\\2.Asset\FOTO\\receh.png') #ubah lokasi file kalian taro yang mau diupload
                pyautogui.press('enter')

                time.sleep(10)
            else:
                print(KeyError)
            break
        except ValueError:
            print('masukan berupa angka')

def main():
    upload()

if __name__ == '__main__' :
    main()




