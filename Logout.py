python
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_login_success(self):
        # Open the web application
        self.driver.get("http://localhost/BadCrud/login")

        # Log in to the web application
        self.driver.find_element_by_name("username").send_keys("valid_username")
        self.driver.find_element_by_name("password").send_keys("valid_password")
        self.driver.find_element_by_name("login").click()
        time.sleep(5)

        # Verify that the user is logged in
        self.assertTrue(self.driver.find_elements_by_name("welcome"))
        self.assertTrue(self.driver.find_elements_by_name("logout"))

    def test_login_failure(self):
        # Open the web application
        self.driver.get("http://localhost/BadCrud/login")

        # Log in to the web application
        self.driver.find_element_by_name("username").send_keys("invalid_username")
        self.driver.find_element_by_name("password").send_keys("invalid_password")
        self.driver.find_element_by_name("login").click()
        time.sleep(5)

        # Verify that the user is not logged in
        self.assertFalse(self.driver.find_elements_by_name("welcome"))
        self.assertFalse(self.driver.find_elements_by_name("logout"))

if __name__ == '__main__':
    unittest.main()
