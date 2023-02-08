import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class PythonContact (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_contact_in_python(self):
        driver = self.driver
        driver.get("https://diaryme.site/")
        driver.maximize_window()
        time.sleep(4)
        target = driver.find_element(By.XPATH, "(//h2[normalize-space()='Contact'])[1]")
        driver.execute_script("arguments[0].scrollIntoView()", target)
        driver.find_element(By.XPATH, "(//input[@id='name'])[1]").send_keys("Liana")
        driver.find_element(By.XPATH, "(//input[@id='email'])[1]").send_keys("pecintasastra55@gmail.com")
        driver.find_element(By.XPATH, "(//input[@id='subject'])[1]").send_keys("Tolong lihat aku")
        driver.find_element(By.XPATH, "(//textarea[@placeholder='Message'])[1]").send_keys("Dan jawab pertanyaanku")
        driver.find_element(By.XPATH, "(//button[normalize-space()='Send Message'])[1]").click()


if __name__ == "__main__":
    unittest.main()