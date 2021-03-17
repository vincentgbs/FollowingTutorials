import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import tkinter as tk

## A simple script to help you signup for a covid vaccine (please make sure you're eligible)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

url = 'https://www.kroger.com/rx/guest/get-vaccinated'

## Download the chromedriver from https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
driver.get(url)

zipCodeElement = driver.find_element_by_xpath("//input[@placeholder='ZIP code, City, State OR Name']")
zip = sys.argv[1]
zipCodeElement.send_keys(zip)
zipCodeElement.send_keys(Keys.TAB);
zipCodeElement.send_keys(Keys.RETURN);

selectStoreElement = driver.find_elements_by_class_name("kds-Button kds-Button--primary kds-Button--compact StoreResult-selectButton")[0] # select the closest store

continueElement = driver.find_elements_by_class_name("kds-Button kds-Button--primary Pharmacy-ContinueButton")[0] # select the first continue button
continueElement.click() # check for available appointments

text = "Sorry, there are no available time slots at this location. Please try another location or check back soon."
while (text in driver.page_source):
    time.sleep(60) # check every minute
    dropStoreElement = driver.find_elements_by_class_name("kds-Icon kds-Icon--interactive text-action-800 kds-Icon--utilityMedium my-auto")[0] # select the dropdown again
    dropStoreElement.click()
    continueElement.click() # check for available appointments

# Not sure what the following screens look like, so this just creates a popup so that you know to switch to the browser and register for the vaccine
window = tk.Tk()
greeting = tk.Label(text="GO SIGN UP ASAP!")
