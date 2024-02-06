from selenium import webdriver
import time

#inisialisasi selenium
driver = webdriver.Chrome()

#buka halaman aplikasi
driver.get(http://localhost/BadCrud/update.php?id=123')

#login
driver.find_element_by_name('username').send_keys('your-username')
driver.find_element_by_name('password').send_keys('your-password')
driver.find_element_by_xpath('//button').click()

#update kontak dengan id tertentu
driver.find_element_by_name('name').send_keys('New Name')
driver.find_element_by_name('email').send_keys('new-email@example.com')
driver.find_element_by_name('phone').send_keys('1234567890')
driver.find_element_by_name('title').send_keys('New Title')
driver.find_element_by_xpath('//input[@type="submit"]').click()

#tunggu beberapa waktu sebelum redirect
time.sleep(3)

#verifikasi apakah kontak telah diupdate
assert 'Contact Updated' in driver.page_source

#verifikasi nilai kontak yang telah diupdate
assert 'New Name' in driver.page_source
assert 'new-email@example.com' in driver.page_source
assert '1234567890' in driver.page_source
assert 'New Title' in driver.page_source

#tutup browser
driver.quit()
