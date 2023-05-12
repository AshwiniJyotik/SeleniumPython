from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)
service_obj = Service("E:\\Selenium with Python\\drivers\\chromedriver_win32 (3)\\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=service_obj)
driver.implicitly_wait(10)
driver.get("https://www.google.com/")
driver.implicitly_wait(10)
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)

driver.find_element(By.ID, 'APjFqb').send_keys("Naveen Automationlabs")
googlesearchlist = driver.find_elements(By.CSS_SELECTOR, "ul.G43f7e li div.wM6W7d span")
print(len(googlesearchlist))
for span_element in googlesearchlist:
    span_text = span_element.text
    print(span_text)
   # print(len(span_text))
    if span_text== 'naveen automationlabs udemy':
        span_element.click()
else:
    print("Option not found")

time.sleep(5)
driver.quit()