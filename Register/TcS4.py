import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class PythonFalseeeRegister (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_falseeeregister_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/register")
        driver.maximize_window()
        elem = driver.find_element(By.XPATH, "(//button[normalize-space()='Register'])[1]")
        elem.click()
        self.driver.save_screenshot("ss1.png")
        self.assertNotIn("Faild.", driver.page_source)


if __name__ == "__main__":
    unittest.main()
