from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class GoogleSearchTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # Убедитесь, что ChromeDriver установлен
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get("https://www.google.com")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("QA Automation")
        search_box.submit()

        self.assertIn("QA Automation", self.driver.title)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
