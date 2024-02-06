from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#inisialisasi webdriver
driver = webdriver.Chrome()

#buka halaman aplikasi
driver.get(' http://localhost/BadCrud/login.php')

#login
driver.find_element_by_name('username').send_keys('your-username')
driver.find_element_by_name('password').send_keys('your-password')
driver.find_element_by_name('submit').click()

#buka halaman create contact
driver.get(http://localhost/BadCrud/create.php')

#isi form create contact
driver.find_element_by_name('name').send_keys('Test Contact')
driver.find_element_by_name('email').send_keys('test@example.com')
driver.find_element_by_name('phone').send_keys('1234567890')
driver.find_element_by_name('title').send_keys('Test Title')

#simpan kontak
driver.find_element_by_name('submit').click()

#tunggu beberapa saat sebelum melakukan pengecekan
time.sleep(3)

#verifikasi apakah kontak telah disimpan
assert 'Test Contact' in driver.page_source

#tutup webdriver
driver.quit()
