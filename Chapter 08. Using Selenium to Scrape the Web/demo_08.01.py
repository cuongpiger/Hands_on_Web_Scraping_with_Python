from selenium import webdriver
import re

driver = webdriver.PhantomJS()
driver.get('https://www.python.org/')

if re.search(r"python.org", driver.current_url):
    driver.save_screenshot("./images/python.org.png") # chụp ảnh màn hình và lưu lại
    print("Đã chụp ảnh màn hình trang python.org")
    
    