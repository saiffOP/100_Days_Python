from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

upcoming_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time ")
upcoming_times_list = [upcoming_event.text for upcoming_event in upcoming_times]

upcoming_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a ")
upcoming_names_list = [upcoming_name.text for upcoming_name in upcoming_names]
events = {}

for n in range(len(upcoming_times)):
    events[n] = {
        "time": upcoming_times_list[n],
        "name": upcoming_names_list[n]
    }

print(events)
driver.quit()

