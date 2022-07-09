import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(5)

# Open the web browser
driver.get('https://testingqarvn.com.es/prueba-de-campos-checkbox/')
time.sleep(1)
button = driver.find_element(By.XPATH,"//label[contains(@id,'wsf-1-label-36-row-1')]")
button.click()
time.sleep(1)

driver.close()