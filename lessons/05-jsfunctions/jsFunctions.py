import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service(executable_path='C:/drivers/chromedriver.exe')
driver = webdriver.Chrome(service=service)

# An amount of time to wait certain component or page
# after this time, and error is trigger

driver.implicitly_wait(15)

# Open the web browser
driver.get('https://ojs.unipamplona.edu.co/ojsviceinves/index.php/bistua/index')
time.sleep(1)
driver.implicitly_wait(15)
button = driver.find_element(By.XPATH,"//*[@id='headerNavigationContainer']/div/div/button")
button.click()
time.sleep(1)

#  Execute js scripts, in this case scroll down
driver.execute_script("window.scrollTo(0,1000)")
driver.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/section[3]/div[2]/div[2]/ul/li/a").click()

time.sleep(1)

driver.close()