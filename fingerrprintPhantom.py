from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import whatsapp
import twilio_call
import unittest
from datetime import datetime
from dotenv import load_dotenv 
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.


load_dotenv('.env')
driver = webdriver.Chrome(
    executable_path=r'E:\Desktop\code\Gecko exe\chromedriver.exe', chrome_options=options
    )
twilio_call.message()

driver.maximize_window()
time.sleep(4)
driver.get('https://urldefense.proofpoint.com/v2/url?u=https-3A__booknow.appointment-2Dplus.com_7ryk7y2x_appointment-5Factions_-3FglobalId-3D7fedde8c617d5d2790395796d3892ccb84c7fff60f0412fd4a99cab9251b3362&d=DwMFAA&c=sJ6xIWYx-zLMB3EPkvcnVg&r=oETJl4cdrdWbZon5OfFj2w&m=j_HOKCyO_t8PfkXI6ZOAoUqKEUcF2tZYn_p9i9BI4iXW4tYyVYPTN7-1dmnai6EO&s=wkY0XuejMWdc0QT2mFAu6HOFV5ouEYap3yteJP-SgcM&e=')
# this is for gainesville DL , goto booking and remote driving test to check for dates 
time.sleep(4)
driver.get('https://booknow.appointment-plus.com/7ryk7y2x/')
time.sleep(4)
select= Select(driver.find_element_by_name('service_id'))
time.sleep(2)
select.select_by_visible_text('FBI Live Scan')
time.sleep(4)
select= Select(driver.find_element_by_name('e_id'))
time.sleep(2)
select.select_by_value('292')
time.sleep(10)
driver.get_screenshot_as_file("screenshot"+str(-1)+".png")


def my_function(c):
    now = datetime.now()
    if "javascript:dosubmit('20220204', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 4th") 
        twilio_call.message() 
    elif "javascript:dosubmit('20220205', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 5th") 
        twilio_call.message() 
    elif "javascript:dosubmit('20220206', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 6th") 
        twilio_call.message()
    elif "javascript:dosubmit('20220207', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 7th") 
        twilio_call.message()
    elif "javascript:dosubmit('20220208', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 8th") 
        twilio_call.message()
    elif "javascript:dosubmit('20220209', 'viewappts', 'no','Child', 1)" in driver.page_source:
        print("success on 9th") 
        twilio_call.message()
    else:
        c=c+1
        # print("fail no: "+str(c))
        current_time = now.strftime("%H:%M:%S")
        print("fail no: "+str(c)+"Current Time ="+ current_time)
        if (c %20 ==0):
            driver.get_screenshot_as_file("screenshot"+str(c)+".png")
        return c


x=0
print("started")
while 1:
    time.sleep(20)
    try:
        x=my_function(x)
        driver.refresh()

    finally:
        time.sleep(3*60)
        driver.refresh()
        time.sleep(5)

    
    