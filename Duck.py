from string import ascii_letters
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

#import text
from datetime import datetime
#import check
#import city
import sys
from sys import exit

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

#driver = webdriver.Chrome(options=options)

driver = webdriver.Firefox(
    executable_path=r'E:\Desktop\code\Gecko exe\geckodriver.exe'
    )
    
driver.implicitly_wait(2)
driver.maximize_window()

driver.get('https://duckduckgo.com/email/choose-address')
#time.sleep(2)
#search = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/button')
#search.click()
#print(driver.find_element_by_xpath("/html/body").text)
"""
rates = driver.find_elements_by_class_name('NFIRFd')
#print (rates)
for i in rates:
    print (rates[i])
"""

#//*[@id="yDmH0d"]/div[6]/div[1]/div[2]/div[1]/div/div[2]/span/div/div[1]/div/c-wiz/div/div/c-wiz/div/div[1]/div[2]/div[1]/div

invite="DFUI78A"
account="srikant"
driver.maximize_window()
driver.get('https://duckduckgo.com/email/choose-address')
time.sleep(5)
search = driver.find_element_by_xpath('//*[@id="inviteCodeInputGroup"]')
search.send_keys(invite)
search = driver.find_element_by_xpath('//*[@id="root"]/main/section/div/div/div[2]/form/label[2]/input')
search.send_keys(account)
search = driver.find_element_by_xpath('//*[@id="root"]/main/section/div/div/div[2]/form/label[3]/input')
search.send_keys("ksrikantiyer33@gmail.com")
search = driver.find_element_by_xpath('//*[@id="root"]/main/section/div/div/div[2]/form/button')
search.click()
#time.sleep(20)
"""
now = datetime.now()
print(account+" "+now.strftime("%H"+":"+"%M"+":"+"%S"))
string=" "
x = 0
n=100
"""
n=10
a=66
while n:
    time.sleep(0)
    try:
        invite="DFWY"+str(n)+chr(a)
        #invite=i+chr(a)
        #count=count+1
        if (n>98):
            n=0
            a=a+1
        search = driver.find_element_by_xpath('//*[@id="inviteCodeInputGroup"]')
        search.clear()
        search.send_keys(invite)
        search = driver.find_element_by_xpath('//*[@id="root"]/main/section/div/div/div[2]/form/button')
        search.click()
        n=n+1
    finally:
        time.sleep(2)
        #driver.refresh()    
    