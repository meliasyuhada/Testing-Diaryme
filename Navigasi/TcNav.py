import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class PythonNav (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_nav_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/")
        driver.maximize_window()
        sleep(2)
        self.driver.save_screenshot("ss1.png") 
        elem = driver.find_element(By.XPATH, "//nav[@id='navbar']//a[normalize-space()='Lihat Karya']")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("ss2.png")
        elem = driver.find_element(By.XPATH, "//nav[@id='navbar']//a[normalize-space()='Kategori']")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("ss3.png")
        elem = driver.find_element(By.XPATH, "//nav[@id='navbar']//a[normalize-space()='Lomba']")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("ss4.png")
        elem = driver.find_element(By.XPATH, "//a[normalize-space()='Log in']")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("ss5.png")
        self.assertNotIn("Faild", driver.page_source)

if __name__ == "__main__":
    unittest.main()