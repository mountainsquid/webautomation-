# Instead of manually going to a website to check the chart
# bot will visit the website and take a screen shot of the chart for you 
# download the pic into your computah!

import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from time import gmtime, strftime

gecko = os.path.join(os.path.abspath("path_to_geckodriver"))
service = FirefoxService(executable_path=gecko)
browser = webdriver.Firefox(service=service)

# Navigate to the website
browser.get("https://www.geckoterminal.com/arbitrum/pools/0x8e89F6D18086BCb660826b6dE0e2a178F6155153")

print("click, brrrr. Script running!")

# Get the full height of the page
height = browser.execute_script("return document.body.scrollHeight")

# Set the browser window size
browser.set_window_size(1920, height)

# Take a screenshot
screenshot = browser.save_screenshot("screenshot.png")

# Generate a unique file name using the current time
time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
screenshot_file = "screenshot_" + time + ".png"

# Save the screenshot to the computer
browser.save_screenshot(screenshot_file)

# Close the browser
browser.quit()
