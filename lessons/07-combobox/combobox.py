import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(5)

# Open the web browser
driver.get('https://testingqarvn.com.es/combobox/')
time.sleep(1)
# Select specify that is a selection field
combo = Select(driver.find_element(By.ID,"wsf-1-field-53"))
combo.select_by_index(1) # select the element by index is the best practice
# the value or name can change in time
time.sleep(1)

driver.close()