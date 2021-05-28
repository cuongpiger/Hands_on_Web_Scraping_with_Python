from selenium import webdriver
import re

driver = webdriver.PhantomJS()

driver.get("https://www.python.org")
print(f">> Title {driver.title}")
print(f">> Page URL {driver.current_url}")

if re.search(r"python.org", driver.current_url):
    driver.save_screenshot("./images/python.org_1.png")
    print("Đã chụp ảnh màn hình trang python.org")
    
cookies = driver.get_cookies()
print(f">> Page source {driver.page_source}")
print(f">> Cookies: {cookies}")

driver.refresh()

driver.get('https://www.google.com')
print(">> Title: ", driver.title)
print(">> Page URL: ", driver.current_url)

if re.search(r'google.com', driver.current_url):
    driver.save_screenshot("./images/google.png")
    print("Đã chụp ảnh màn hình google.com")
    
cookies = driver.get_cookies()
print(f">> Cookies: {cookies}")

print(f"Current URL {driver.current_url}")
driver.back()
print(f">> Back URL {driver.current_url}")
driver.forward()
print(f">> Forward URL {driver.current_url}")

driver.close()
driver.quit()