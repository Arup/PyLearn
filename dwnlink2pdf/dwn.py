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
#browser = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome(chromedriver)
driver.get('https://www.google.com/')
driver.execute_script('window.print();')
