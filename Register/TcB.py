import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


class PythonTrueCRUD (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_truecrud_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/register")
        driver.maximize_window()
        elem = driver.find_element(By.XPATH, "(//input[@id='name'])[1]")
        elem.send_keys("Mazura")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='email'])[1]")
        elem.send_keys("technology.secret55@gmail.com")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='password'])[1]")
        elem.send_keys("12345678")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='password-confirm'])[1]")
        elem.send_keys("12345678")
        time.sleep(3)
        self.driver.save_screenshot("ss1.png")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot("ss2.png")
        time.sleep(3)
        self.assertNotIn("Faild.", driver.page_source)


if __name__ == "__main__":
    unittest.main()
