import selenium
import undetected_chromedriver
import time
import requests

driver = undetected_chromedriver.Chrome(driver_executable_path="C:\\Users\\Thomas\\OneDrive\\Apps\\Documents\\GitHub\\Narcissus\\Narcisuss\\chromedriver.exe")
while True:
    driver.get("https://github.com/ThomasGust/ThomasGust")
    time.sleep(1)
