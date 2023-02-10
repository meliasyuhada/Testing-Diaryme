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
        driver.get("https://diaryme.site/")
        driver.maximize_window()
        sleep(2)
        self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\image\ss1.png")
        target = driver.find_element(By.XPATH, "(//h2[normalize-space()='Karya'])[1]")
        driver.execute_script("arguments[0].scrollIntoView()", target)
        sleep(2)
        self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\image\ss2.png")
        elem = driver.find_element(By.XPATH, "(//img[@src='https://diaryme.site/public/images/cake.jpg'])[1]")
        elem.click()
        sleep(2)
        self.driver.save_screenshot("C:\python_selenium\PythonSeleniumProject1\Testing-Diaryme\ss\image\ss3.png")
        self.assertNotIn("Faild", driver.page_source)

if __name__ == "__main__":
    unittest.main()