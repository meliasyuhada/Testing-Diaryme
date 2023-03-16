import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


class PythonFalseeeRegister (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_falseeeregister_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/register")
        driver.maximize_window()
        elem = driver.find_element(By.XPATH, "(//input[@id='name'])[1]")
        elem.send_keys("Mazura005 liana jaya purna purnama kertajasa putra bungsu ruana jaya karta")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='email'])[1]")
        elem.send_keys("jayapura@ada.saja")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='password'])[1]")
        elem.send_keys("123456789098765")
        time.sleep(3)
        elem = driver.find_element(By.XPATH, "(//input[@id='password-confirm'])[1]")
        elem.send_keys("123456785432145")
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
