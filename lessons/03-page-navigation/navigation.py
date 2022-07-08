import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)


# Open the web browser
driver.get('https://testingqarvn.com.es/')
time.sleep(1)

driver.get('https://testingqarvn.com.es/datos-personales/')
time.sleep(1) # With this time the navigator works


driver.back() 
time.sleep(1)
driver.forward()
time.sleep(1)
driver.close()

