from selenium import webdriver
import time

#inisialisasi selenium
driver = webdriver.Chrome()

#buka halaman aplikasi
driver.get(' http://localhost/BadCrud/index.php')

#login
driver.find_element_by_name('username').send_keys('your-username')
driver.find_element_by_name('password').send_keys('your-password')
driver.find_element_by_xpath('//button').click()

#hapus kontak dengan id tertentu
driver.get(‘http://localhost/BadCrud//delete.php?id=123')

#tunggu beberapa waktu sebelum redirect
time.sleep(3)

#verifikasi apakah kontak telah dihapus
assert 'Contact Deleted' in driver.page_source

#tutup browser
driver.quit()
