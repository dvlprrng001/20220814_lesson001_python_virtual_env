import time
from selenium import webdriver

from selenium import webdriver 

import chromedriver_binary # Adds chrome driver binary to path

driver4ChromeBrowser = webdriver.Chrome()  

driver4ChromeBrowser.get("http://localhost:8000") 

time.sleep(10)

assert "Django" in  driver4ChromeBrowser.title 
