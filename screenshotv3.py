# UPDATED for previous error handling
# Since I don't know how to edit a push (yet)
# I will manually create a new file 
# Would be cool to run a VPS and run as a cron job 

import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import gmtime, strftime

gecko = os.path.join(os.path.abspath("path_to_geckodriver"))
service = FirefoxService(executable_path=gecko)
browser = webdriver.Firefox(service=service)

# Navigate to the website
browser.get("https://www.cnn.com")

print("click, brrrr. Script running!")

# Take a screenshot
screenshot = browser.save_screenshot("screenshot.png")

# Generate a unique file name using the current time
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
screenshot_file = "screenshot_" + time + ".png"

# Save the screenshot to the computer
browser.save_screenshot(screenshot_file)

# Close the browser
browser.quit()
