import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

class PythonLogin(unittest.TestCase):
     def setUp(self):
        self.driver = webdriver.Chrome()

     def test_login_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/login")
        driver.maximize_window()
        self.assertIn("Laravel", driver.title)
        elem = driver.find_element(By.XPATH, "//input[@id='email']")
        elem.send_keys()
        elem = driver.find_element(By.XPATH, "//input[@id='password']")
        elem.send_keys()
      #   self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\login\ss5.png")
        elem = driver.find_element(By.XPATH, "//button[normalize-space()='Login']")
        elem.click()
      #   self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\login\ss6.png")
        self.assertNotIn("Faild.", driver.page_source)

if __name__ == "__main__":
    unittest.main()