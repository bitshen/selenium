from selenium import webdriver
from selenium.webdriver.firefox.options import Options  # 导入Firefox的Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager  # 导入GeckoDriverManager
from selenium.webdriver.firefox.service import Service  # 导入Firefox的Service

def test_eight_components():
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # 配置Firefox无头模式
    firefox_options.add_argument("--no-sandbox")  # 在Docker容器中运行时需要
    firefox_options.add_argument("--disable-dev-shm-usage")  # 限制Docker使用的内存量
    
    # 使用GeckoDriverManager自动管理Geckodriver
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    title = driver.title
    print(f"页面标题为：'{title}'")  # 打印页面标题
    assert title == "Web form", f"期望的页面标题为'Web form'，但实际为'{title}'"

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="my-text")
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    
    # driver.get_screenshot_as_file("/app/screenshots/example_com_screenshot.png")
    driver.save_screenshot('/app/screenshots/example_com_screenshot.png')
    
    text_box.send_keys("Selenium")
    print("在文本框中输入了'Selenium'")  # 打印操作信息
    submit_button.click()
    print("点击了提交按钮")  # 打印操作信息

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    print(f"消息内容为：'{value}'")  # 打印消息内容
    assert value == "Received!", f"期望的消息内容为'Received!'，但实际为'{value}'"

    driver.quit()
    print("测试完成，浏览器已关闭")  # 打印测试完成信息

# 如果直接运行此脚本，则执行测试
if __name__ == "__main__":
    print("测试开始")
    test_eight_components()
