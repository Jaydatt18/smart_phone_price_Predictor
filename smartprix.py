from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


s = Service('C:/Users/ok/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')
driver = webdriver.Chrome(service = s)
time.sleep(1)
driver.get('https://www.smartprix.com/mobiles')
time.sleep(1)
driver.find_element(by = By.XPATH , value = '/html/body/div/main/aside/div/div[5]/div[2]/label[1]/input').click()
time.sleep(1)
driver.find_element(by = By.XPATH , value='/html/body/div/main/aside/div/div[5]/div[2]/label[2]/input').click()
time.sleep(1)
# old_height = driver.find_element(by=By.XPATH , value = '/html/body/div/main/div[1]/div[2]/div[3]').click()
old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    driver.find_element(by=By.XPATH , value='//*[@id="app"]/main/div[1]/div[2]/div[3]').click()
    time.sleep(1)
    new_height = driver.execute_script('return document.body.scrollHeight')
    print(old_height)
    print(new_height)

    if old_height == new_height :
        break
    old_height = new_height

html = driver.page_source
with open('smart1.html' , 'w' , encoding='utf-8') as f:
    f.write(html)

time.sleep(8)

