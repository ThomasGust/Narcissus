import selenium
import undetected_chromedriver
import time
import requests
import sys
import random

"""
This is a simple toy script to give a GitHub profile more views. Command line usage will be described in the README for this repository.
"""

print("STARTED")
options = undetected_chromedriver.ChromeOptions()

# RIGHT NOW, HEADLESS DOES NOT ACTUALLY REGISTER NEW VIEWS
if int(sys.argv[4]) == 1:
    print("ATTEMPTING TO HIDE")
    #options.add_argument("--headless")
    options.add_argument("--no-startup-window")
    options.add_argument('-no-sandbox')

username = sys.argv[1]
refresh_lag = int(sys.argv[2])
profile_path = f"https://github.com/{username}/{username}"
n = int(sys.argv[3])

driver = undetected_chromedriver.Chrome(driver_executable_path="chromedriver.exe", options=options, subprocess=True)
driver.get(profile_path)

counted = 0

if n == 0:
    while True:
        wt = random.choice([refresh_lag+random.uniform(0, refresh_lag*0.1), refresh_lag-random.uniform(0, refresh_lag*0.1)])
        try:
            #driver.get(profile_path)
            driver.execute_script("location.reload()")
            time.sleep(wt)
        except Exception as e:
            if type(e) != KeyboardInterrupt:
                driver = undetected_chromedriver.Chrome(driver_executable_path="chromedriver.exe", options=options, use_subprocess=True)
                driver.get(profile_path)
                time.sleep(wt)
            else:
                break
else:
    while counted <= n:
        wt = random.choice([refresh_lag+random.uniform(0, refresh_lag*0.1), refresh_lag-random.uniform(0, refresh_lag*0.1)])
        try:
            #driver.get(profile_path)
            driver.execute_script("location.reload()")
            time.sleep(wt)
        except Exception as e:
            if type(e) != KeyboardInterrupt:
                driver = undetected_chromedriver.Chrome(driver_executable_path="chromedriver.exe", options=options, use_subprocess=True)
                driver.get(profile_path)
                time.sleep(wt)
            else:
                break
        counted += 1
