　　from selenium import webdriver

　　import base64
　　driver = webdriver.Chrome()
　　driver.get('https://www.baidu.com/')
　　# 通过base64进行保存图片
　　x = driver.get_screenshot_as_base64()
　　image = base64.b64decode(x)
　　file = open('1.jpg', "wb")
　　file.write(image)
