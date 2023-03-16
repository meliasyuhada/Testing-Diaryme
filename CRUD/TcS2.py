import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
import time


class PythonFalseeCRUD (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_falseecrud_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/login")
        driver.maximize_window()
        self.assertIn("Laravel", driver.title)
        elem = driver.find_element(By.XPATH, "//input[@id='email']")
        elem.send_keys("userdiaryme@gmail.com")
        elem = driver.find_element(By.XPATH, "//input[@id='password']")
        elem.send_keys("12345678")
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\ss1.png")
        time.sleep(3)
        elem = driver.find_element(
            By.XPATH, "//button[normalize-space()='Login']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\ss2.png")
        elem = driver.find_element(
            By.XPATH, "//i[@class='bi bi-chevron-down ms-auto']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\ss3.png")
        elem = driver.find_element(
            By.XPATH, "//span[normalize-space()='Data']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\ss4.png")
        elem = driver.find_element(
            By.XPATH, "//a[normalize-space()='Add Post']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\ss5.png")
        elem = driver.find_element(
            By.XPATH, "(//button[normalize-space()='Publish'])[1]")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s2\s11.png")
        self.assertNotIn("Faild.", driver.page_source)


if __name__ == "__main__":
    unittest.main()
