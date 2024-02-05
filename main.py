import selenium
import undetected_chromedriver
import time
import requests
import sys


if __name__ == "__main__":
    options = uc.ChromeOptions()
    if sys.argv[4] == 1:
        options.add_argument("--headless")

    username = sys.argv[1]
    refresh_lag = sys.argv[2]
    profile_path = f"https://github.com/{username}/{username}"
    n = sys.argv[3]

    driver = undetected_chromedriver.Chrome(driver_executable_path="chromedriver.exe", options=options, use_subprocess=True)

    counted = 0

    if n == 0:
        while True:
            driver.get(profile_path)
            time.sleep(refresh_lag)
    else:
        while counted <= n:
            driver.get(profile_path)
            time.sleep(refresh_lag)

