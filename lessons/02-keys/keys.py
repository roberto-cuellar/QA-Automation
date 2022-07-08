import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Selection and complete forms using tab
# Open the web browser
driver.get('https://testingqarvn.com.es/datos-personales/')
# Maximice the window
driver.maximize_window()
time.sleep(1)
# Selection by ID
input = driver.find_element(By.ID,'wsf-1-field-21') # Actual input field
# Write some in the input field and jump to other field using tab
input.send_keys('Roberto Antonio'+Keys.TAB+'Cuellar Lozano'+Keys.TAB+'test@test.com'+Keys.TAB+'2343211'+Keys.TAB+'Crra 9 N°20-21')
# Click event in a button
driver.find_element(By.XPATH,"//button[contains(@id,'wsf-1-field-27')]").click()


time.sleep(2)
# Close the web browser
driver.close()
