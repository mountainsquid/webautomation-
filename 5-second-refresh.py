# this script automatically opens firefox and reloads every 5 second until the end of time 

import time 
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import gmtime, strftime

gecko = os.path.join(os.path.abspath("path_to_geckodriver"))
service = FirefoxService(executable_path=gecko)
browser = webdriver.Firefox(service=service)

# Navigate to the website
browser.get("https://boards.4channel.org/g")

print("click, brrrr. Script running!")

while True:
    browser.refresh()
    time.sleep(5)
