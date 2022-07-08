import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)


# Open the web browser
driver.get('https://ojs.unipamplona.edu.co/ojsviceinves/index.php/bistua/index')
time.sleep(1)

# With this explicit wait, we wait until some expected condition is fulfilled
# in the range of 0 to T seconds
button = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH,"//*[@id='headerNavigationContainer']/div/div/button")))

button.click()
time.sleep(1)

driver.close()
