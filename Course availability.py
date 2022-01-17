from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import whatsapp
from datetime import datetime
from tkinter import *
import datetime
import time
import winsound

driver = webdriver.Firefox(
    executable_path=r'E:\Desktop\code\Gecko exe\geckodriver.exe'
    )

driver.maximize_window()
driver.get('<website>')
time.sleep(5)
search = driver.find_element_by_id("username")
search.send_keys("<username>")
search = driver.find_element_by_id("password")
search.send_keys("<password>")
search.send_keys(Keys.RETURN)


time.sleep(50)

def my_function(c):
    
    left=driver.find_element_by_xpath("//*[contains( text(),'')]")
    if 'Seat' in left.text:
        print("Seat") 
        whatsapp.message("Seat Awailable now") 
      
    
    elif 'Wait' in left.text:
        print("Wait")
        while (1): 
            winsound.PlaySound("Welcome.wav",winsound.SND_FILENAME)
        whatsapp.message("Waiting list available ") 


    else:
        
        print ("fail"+ c)
        search = driver.find_element_by_id("instructor")
        search.send_keys(Keys.DELETE)
        return c+1    



def my_function2(c):
    search = driver.find_element_by_id("instructor")
    search.send_keys(" ")
    search.send_keys(Keys.RETURN)
    time.sleep(5)
    search.send_keys(Keys.DELETE)
    return c
    
    
    

        
x=0
print ("started")
while 1:

    time.sleep(5)
    try:
        x=my_function(x)
    finally:
        time.sleep(5)
        x=my_function2(x)
    
    