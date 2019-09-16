import json
from selenium import webdriver
import os
os.environ["LANG"] = "en_US.UTF-8"

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

profile = {'printing.print_preview_sticky_settings.appState': json.dumps(appState)}


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('prefs', profile)
chrome_options.add_argument('--kiosk-printing')

chromedriver = '/usr/local/bin/chromedriver'
options = webdriver.ChromeOptions()
#browser = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome(chromedriver)
#options.add_argument("headless")

filename1="./leetcodedotcomProblems.txt"
with open(filename1) as f:
    lines = f.readlines()
i=0
for l in lines:
    p = str(i) + 'image.png'
    if(i<1):
      #driver.get(l)
      driver.get(l)
      #driver.get_screenshot_as_file('/tmp/google.png')
      driver.get_screenshot_as_png(p)
      #driver.execute_script('window.print();')
    i=i+1
