from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import whatsapp
from datetime import datetime

# s=Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=s)

driver = webdriver.Chrome(
    executable_path=r'E:\Desktop\code\Gecko exe\chromedriver.exe'
    )

driver.maximize_window()
driver.get('https://book.appointment-plus.com/6kznhmqx#/?_qk=g5p8216lsp8')
time.sleep(10)
# search = driver.find_element_by_id("username")
# search.send_keys("<username>")
# search = driver.find_element_by_id("password")
# search.send_keys("<password>")

# time.sleep(20)


def my_function(c):
    if "1/19" in driver.page_source:
        print("success") 
        whatsapp.message("Trial No"+str(c)+": 1/19") 

    elif "1/26" in driver.page_source:
        print("success") 
        whatsapp.message("Trial No"+str(c)+": 1/26 ") 


    else:
        c=c+1
        print("fail no: "+str(c))
        return c


x=0
print("started")
while 1:
    time.sleep(20)
    try:
        x=my_function(x)
        driver.refresh()

    finally:
        time.sleep(30)
        driver.refresh()
        time.sleep(5)

    
    