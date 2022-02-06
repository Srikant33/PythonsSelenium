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

#driver.get('https://www.siteyaar.com/gmail-availability-checker')
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

invite="sri"
account="srikant"
driver.maximize_window()
driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp')
time.sleep(5)
#search.send_keys(invite)
search = driver.find_element_by_xpath('//*[@id="firstName"]')
search.send_keys("Santosh")
search = driver.find_element_by_xpath('//*[@id="lastName"]')
search.send_keys("Iyer")
#search = driver.find_element_by_xpath('//*[@id="root"]/main/section/div/div/div[2]/form/button')
#search.click()
#time.sleep(20)

"""
now = datetime.now()
print(account+" "+now.strftime("%H"+":"+"%M"+":"+"%S"))
string=" "
x = 0
n=100
"""
n=0
text="That username is taken"
while n<1000:
    time.sleep(0)
    try:
        search = driver.find_element_by_xpath('//*[@id="username"]')
        
        if (n<10):
            invite="san"+"00"+str(n)
        elif(n<100):
            invite="san"+"0"+str(n)
        else:
            invite="san"+str(n)
        
        search.clear()
        search.send_keys(invite)
        
        #invite=i+chr(a)
        #count=count+1
        """if (n>98):
            n=0
            a=a+1
        """
        search = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[3]/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input').click()
        
        #issue= driver.is_element_exist('/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div')
        time.sleep(1)
        if text in driver.page_source:
            pass
        else:
            print(invite)
       
        """
        search.clear()
        search.send_keys(invite)
        """
        n=n+1
    finally:
        pass
        #driver.refresh()    
    