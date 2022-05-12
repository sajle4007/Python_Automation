from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

ticket_amount=driver.find_element(By.XPATH,"//input[@id='product_549']")
ticket_amount.click()
ticket_amount1="1,200"
time.sleep(2)

first_name=driver.find_element(By.XPATH,"//input[@id='travname']")
first_name.send_keys("saaaaaaaj")
time.sleep(1)

last_name=driver.find_element(By.XPATH,"//input[@id='travlastname']")
last_name.send_keys("cpppp")
time.sleep(1)

date_input=driver.find_element(By.XPATH,"//input[@id='dob']")
date_input.click()

month=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
month.click()
month_list=Select(month)
month_list.select_by_visible_text("May")
time.sleep(1)

year=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
year.click()
year_list=Select(year)
year_list.select_by_value("1990")
time.sleep(1)

day=driver.find_element(By.XPATH,"//a[normalize-space()='20']")
day.click()

gender=driver.find_element(By.XPATH,"//input[@id='sex_1']")
gender.click()

travel_type=driver.find_element(By.XPATH,"//input[@id='traveltype_1']")
travel_type.click()

from_city=driver.find_element(By.XPATH,"//input[@id='fromcity']")
from_city.send_keys("Calicut")

destination=driver.find_element(By.XPATH,"//input[@id='tocity']")
destination.send_keys("Dubai")

departure_date=driver.find_element(By.XPATH,"//input[@id='departon']")
departure_date.click()

month1=driver.find_element(By.XPATH,"//select[@aria-label='Select month']")
month1.click()
month1_list=Select(month1)
month1_list.select_by_visible_text("Aug")
time.sleep(1)

year1=driver.find_element(By.XPATH,"//select[@aria-label='Select year']")
year1.click()
year1_list=Select(year1)
year1_list.select_by_visible_text("2023")

dep_day=driver.find_element(By.XPATH,"//a[normalize-space()='30']")
dep_day.click()



application_purpose=driver.find_element(By.XPATH,"//*[@id='reasondummy']")
options=Select(application_purpose)

options.select_by_visible_text("Expedite passport renewal")

time.sleep(1)

recieve_method=driver.find_element(By.XPATH,"//input[@id='deliverymethod_1']")
recieve_method.click()

bill_name=driver.find_element(By.XPATH,"//input[@id='billname']")
bill_name.send_keys("kkk")

ph=driver.find_element(By.XPATH,"//input[@id='billing_phone']")
ph.send_keys("9887744556")

email=driver.find_element(By.XPATH,"//input[@id='billing_email']")
email.send_keys("abc@gmail.com")

country=driver.find_element(By.XPATH,"//*[@id='billing_country']")
country_opt=Select(country)
country_opt.select_by_visible_text("India")



adress=driver.find_element(By.XPATH,"//input[@id='billing_address_1']")
adress.send_keys("aaaaaaaaaaaaaaaaaaaaa1234")

town=driver.find_element(By.XPATH,"//input[@id='billing_city']")
town.send_keys("cochin")

state=driver.find_element(By.XPATH,"//*[@id='billing_state']")
state_opt=Select(state)
state_opt.select_by_visible_text("Kerala")

pin=driver.find_element(By.XPATH,"//input[@id='billing_postcode']")
pin.send_keys("444456")

final_amount=driver.find_element(By.XPATH,"//*[@id='order_review']/div[1]/table/tfoot/tr[2]/td/strong/span")
print(final_amount.text[1:])
print(ticket_amount1)
if ticket_amount1==final_amount.text[1:]:
    print("Net total is same")
else:
    print("incorrect net amount")

driver.quit()







