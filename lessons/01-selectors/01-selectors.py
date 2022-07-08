import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Select different elements using all kinds of selector posibilities

# Open the web browser
driver.get('https://testingqarvn.com.es/datos-personales/')
# Maximice the window
driver.maximize_window()
time.sleep(1)

# Selection by ID
input = driver.find_element(By.ID,'wsf-1-field-21') # Actual input field
# Write some in the input field
input.send_keys('Hola hola')

# Selection by xpath
apellidos = driver.find_element(By.XPATH,"//input[@id='wsf-1-field-22']")
apellidos.send_keys('cuellar lozano')



time.sleep(1)


# Close the web browser
driver.close()
