from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#inisialisasi webdriver
driver = webdriver.Chrome()

#buka halaman login
driver.get(http://localhost/BadCrud/update.php?id=123')

#isi username dan password
username_field = driver.find_element_by_name('username')
password_field = driver.find_element_by_name('password')
username_field.send_keys('your-username')
password_field.send_keys('your-password')

#klik tombol login
login_button = driver.find_element_by_name('login')
login_button.click()

#tunggu halaman profil dimuat
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'profile-page')))

#cari elemen input file
image_input = driver.find_element_by_name('image')

#pilih file gambar
image_input.send_keys('/path/to/your/image.jpg')

#cari tombol ganti
change_button = driver.find_element_by_name('change')
change_button.click()

#tunggu halaman profil dimuat ulang
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'profile-page')))

#cek apakah gambar profil telah berubah
new_image = driver.find_element_by_id('profile-image')
if new_image.get_attribute('src') == '/path/to/your/image.jpg':
    print('Test case passed')
else:
    print('Test case failed')

#tutup webdriver
driver.quit()
