from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://www.orangehrm.com/")
driver.maximize_window()

free_trial=driver.find_element(By.XPATH,"//input[@id='linkadd']")
free_trial.click()


fav_url=driver.find_element(By.XPATH,"//input[@id='Form_submitForm_subdomain']")
fav_url.send_keys("techolas")

full_name=driver.find_element(By.XPATH,"//input[@id='Form_submitForm_Name']")
full_name.send_keys("sajle")

email_id=driver.find_element(By.XPATH,"//input[@id='Form_submitForm_Email']")
email_id.send_keys("sajle4007@gmail.com")

ph_no=driver.find_element(By.XPATH,"//input[@id='Form_submitForm_Contact']")
ph_no.send_keys("9895194007")

country=driver.find_element(By.XPATH,"//select[@id='Form_submitForm_Country']")
country_list=Select(country)
country_list.select_by_value("India")

state=driver.find_element(By.XPATH,"//select[@id='Form_submitForm_State']")
state_list=Select(state)
state_list.select_by_value("Kerala")


check_box=driver.find_element(By.XPATH,"//*[@id=recaptcha-anchor]/div[1]")
print("default status",check_box.is_selected())
time.sleep(2)
check_box.click()
time.sleep(2)
print("status after click",check_box.is_selected())

submit=driver.find_element(By.XPATH,"//input[@id='Form_submitForm_action_request']")
submit.click()
driver.quit()



