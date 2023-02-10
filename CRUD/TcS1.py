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
        driver.get("https://diaryme.site/login")
        driver.maximize_window()
        self.assertIn("Laravel", driver.title)
        elem = driver.find_element(By.XPATH, "//input[@id='email']")
        elem.send_keys("userdiaryme@gmail.com")
        elem = driver.find_element(By.XPATH, "//input[@id='password']")
        elem.send_keys("12345678")
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss1.png")
        time.sleep(3)
        elem = driver.find_element(
            By.XPATH, "//button[normalize-space()='Login']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss2.png")
        elem = driver.find_element(
            By.XPATH, "//i[@class='bi bi-chevron-down ms-auto']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss3.png")
        elem = driver.find_element(
            By.XPATH, "//span[normalize-space()='Data']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss4.png")
        elem = driver.find_element(
            By.XPATH, "//a[normalize-space()='Add Post']")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss5.png")
        elem = driver.find_element(By.ID, "cover")
        elem.send_keys("D:\Kuliah\kode\disain web kuliah\minggu ketiga\link1.html")
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss6.png")
        elem = driver.find_element(By.XPATH, "//input[@name='title']")
        elem.send_keys("Lingkungan")
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss7.png")
        elem = driver.find_element(By.XPATH, "(//textarea[@id='desc'])[1]")
        elem.send_keys("Jangkauan Mendalam")
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss8.png")
        elem = Select(driver.find_element(By.ID, "category"))
        elem.select_by_visible_text('Non-Fiksi')
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss9.png")
        elem = Select(driver.find_element(By.ID, "tag"))
        elem.select_by_visible_text('cerpen')
        time.sleep(3)
        self.driver.save_screenshot(
            "C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\crud\s1\ss10.png")
        elem = driver.find_element(
            By.XPATH, "(//button[normalize-space()='Publish'])[1]")
        elem.click()
        time.sleep(3)
        self.driver.save_screenshot("s11.png")
        self.assertNotIn("Faild.", driver.page_source)


if __name__ == "__main__":
    unittest.main()
