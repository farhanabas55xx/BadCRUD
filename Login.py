from selenium importdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#inisialisasi browser
browser = webdriver.Chrome()

#membuka halaman login
browser.get(http://localhost/BadCrud/login.php')

#test case login berhasil
def test_case_success_login():
    #isikan username dan password
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'inputUsername'))).send_keys('tester')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'inputPassword'))).send_keys('tester123')

    #klik tombol sign in
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'button'))).click()

    #verifikasi halaman index
    assert 'hk &copy; 2023' in browser.page_source

#test case login gagal
def test_case_failed_login():
    #isikan username dan password
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'inputUsername'))).send_keys('tester')
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, 'inputPassword'))).send_keys('wrong_password')

    #klik tombol sign in
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'button'))).click()

    #verifikasi notifikasi error
    error_message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'checkbox')))
    assert 'Wrong usename or password' in error_message.text

#jalankan test case
test_case_success_login()
test_case_failed_login()

#tutup browser
time.sleep(3)
browser.quit()
