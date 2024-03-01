from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 导入缺失的Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service  # 导入Service类
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True
service = Service(executable_path=GeckoDriverManager().install())  # 使用Service对象
driver = webdriver.Firefox(options=options, service=service)

driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element("name", "q")  # 更新了find_element的调用方式
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
