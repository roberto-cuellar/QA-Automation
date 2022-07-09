import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get('https://pixabay.com/')

try:
    buscar = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,"//a[@href='/images/search/?order=ec']"))) # Wait until visibility
    buscar = driver.find_element(By.XPATH,"//a[@href='/images/search/?order=ec']") # Select the element
    # if we need scroll to there
    go = driver.execute_script("arguments[0].scrollIntoView();",buscar)
    time.sleep(2)
    buscar.click()
except TimeoutException as ex: 
    print('No se encontró el elemento')
finally: 
    driver.close()