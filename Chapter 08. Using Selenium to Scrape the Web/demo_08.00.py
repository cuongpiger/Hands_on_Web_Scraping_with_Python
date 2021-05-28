from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.PhantomJS()
driver.get('https://www.python.org/')

print(f">> Title: {driver.title}")
print(f">> Page URL: {driver.current_url}")
