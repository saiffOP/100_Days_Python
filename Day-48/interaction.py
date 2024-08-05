from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# # article_count.click()
#
# all_portals = driver.find_elements(By.LINK_TEXT, value="Content Portals")
# all_portals.click()
# driver.quit()

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Mohammed Saif")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Shirgaonkar")

email = driver.find_element(By.NAME, value="email")
email.send_keys("saifshirgaonkar1786@gmail.com")

signup_button = driver.find_element(By.CLASS_NAME, value="btn-block")
signup_button.click()
