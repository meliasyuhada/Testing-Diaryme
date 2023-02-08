import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class PythonLihat (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_lihat_in_python (self):
        driver = self.driver
        driver.get("http://project-ubah.open/karya")
        driver.maximize_window()
        sleep(2)
        self.driver.save_screenshot("ss1.png")
        elem = driver.find_element(By.XPATH, "(//img[@class='img-fluid'])[1]")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("ss2.png")
        self.assertNotIn("Faild", driver.page_source)

if __name__ == "__main__":
    unittest.main()