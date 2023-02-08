import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonLogin(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()

     def test_login_in_python(self):
        driver = self.driver
        driver.get("http://project-ubah.open/login")
        driver.maximize_window()
        self.assertIn("Laravel", driver.title)
        elem = driver.find_element(By.XPATH, "//input[@id='email']")
        elem.send_keys("admin@gmail.com")
        elem = driver.find_element(By.XPATH, "//input[@id='password']")
        elem.send_keys("1234")
        self.driver.save_screenshot("ss10.png")
        elem = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        elem.click()
        self.driver.save_screenshot("ss11.png")
        self.assertNotIn("Faild.", driver.page_source)

if __name__ == "__main__":
    unittest.main()