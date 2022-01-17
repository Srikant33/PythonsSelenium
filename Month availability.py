from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import whatsapp
from datetime import datetime

driver = webdriver.Firefox(
    executable_path=r'E:\Desktop\code\Gecko exe\geckodriver.exe'
    )

driver.maximize_window()
driver.get('https://one.uf.edu/soc/registration-search/2221?term=%222221%22&category=%22CWSP%22&prog-level=%22GRAD%22&dept=%2219140000%22')
time.sleep(10)
search = driver.find_element_by_id("username")
search.send_keys("<username>")
search = driver.find_element_by_id("password")
search.send_keys("<password>")

time.sleep(20)


def my_function(c):
    left= driver.find_element_by_id("<element id>")
    now = datetime.now()
    if 'June' in left.text or 'July' in left.text or 'August' in left.text:
        print("success") 
        whatsapp.message("Trial No"+str(c)+": "+left.text[-54:-1]+" at "+ now.strftime("%H"+":"+"%M"+":"+"%S")) 
      
    else:
        c=c+1
        print("fail no: "+str(c)+"  "+left.text[-16:-1]+" at "+now.strftime("%H"+":"+"%M"+":"+"%S"))
        return c

x=0
while 1:
    time.sleep(20)
    try:
        x=my_function(x)
    finally:
        time.sleep(15*60)
        driver.refresh()
    
    