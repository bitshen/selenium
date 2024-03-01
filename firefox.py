import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

class TestWebForm(unittest.TestCase):

    def setUp(self):
        # 测试前的设置
        firefox_options = Options()
        firefox_options.add_argument("--headless")
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    def test_eight_components(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        title = self.driver.title
        self.assertEqual("Web form", title, f"期望的页面标题为'Web form'，但实际为'{title}'")

        text_box = self.driver.find_element(by=By.NAME, value="my-text")
        submit_button = self.driver.find_element(by=By.CSS_SELECTOR, value="button")

        text_box.send_keys("Selenium")
        submit_button.click()

        message = self.driver.find_element(by=By.ID, value="message")
        value = message.text
        self.assertEqual("Received!", value, f"期望的消息内容为'Received!'，但实际为'{value}'")

    def tearDown(self):
        # 测试后的拆解
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
