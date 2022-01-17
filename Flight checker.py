from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

#import text
from datetime import datetime
#import check
#import city
import sys
from sys import exit

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(2)
driver.maximize_window()

driver.get('https://www.google.com/travel/flights/search?tfs=CBwQAhovagwIAhIIL20vMGRsdjASCjIwMjEtMDgtMDlyBwgBEgNHTlaCAQNGUkGCAQNDREdwAYIBCwj___________8BQAFIAZgBAg&tfu=EgYIAhABGAA')
#time.sleep(2)
search = driver.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz[2]/div/div[2]/div/c-wiz/div/c-wiz/div[2]/div[3]/div/div[2]/div[2]/div[2]/div/div/div[1]/button')
search.click()
print(driver.find_element_by_xpath("/html/body").text)
