# Opens Firefox and takes a screenshot of the the website
# Saves the screenshot with a time stamp 
# Good for gathering intel on someone's social media? 
# Maybe you can run this as a CRON job lol

import os
from selenium import webdriver
from time import gmtime, strftime

gecko = os.path.join(os.path.abspath("path_to_geckodriver"))

browser = webdriver.Firefox(executable_path=gecko)

# Navigate to the website
browser.get("https://boards.4channel.org/biz/")

print("click, brrrr")

# Take a screenshot
screenshot = browser.save_screenshot("screenshot.png")

# Generate a unique file name using the current time
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
screenshot_file = "screenshot_" + time + ".png"

# Save the screenshot to the computer
browser.save_screenshot(screenshot_file)

# Close the browser
browser.quit()
