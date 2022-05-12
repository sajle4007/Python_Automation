# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# table_row=print(len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody/tr")))
# table_column=print(len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody/tr/th")))
#
# driver.quit()


                                 #To print the table contents
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

text1=driver.find_element(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody/tr[5]/td[2]")
print(text1.text)

table=driver.find_elements(By.XPATH,"//*[@id='HTML1']/div[1]/table/tbody")
for i in table:
    print(i.text)

# for i in range(2,8):
#     for j in range(1,5):
#         xpath=f"//table[@name='BookTable']/tbody/tr[{i}]/td[{j}]"
#         xpath_element = driver.find_element(By.XPATH,xpath )
#         print(xpath_element.text,end="  ")
#     print()

for i in range(2,8):
    xpath=f"//table[@name='BookTable']/tbody/tr[{i}]/td[2]"
    xpath_element = driver.find_element(By.XPATH,xpath )
    if xpath_element.text=="Amit":
        book=driver.find_element(By.XPATH,f"//table[@name='BookTable']/tbody/tr[{i}]/td[3]")
        print(xpath_element.text,book.text)

driver.quit()
#
# row_2=driver.find_elements(By.XPATH,"//body[1]/div[4]/div[2]/div[2]/div[2]/footer[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]")
# for i in row_2:
#     print(i.text)

                              #table problem Orange HRM

# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
#
# username=driver.find_element(By.XPATH,"//input[@id='txtUsername']")
# # username.clear()
# username.send_keys("Admin")
# # time.sleep(1)
#
# password=driver.find_element(By.XPATH,"//input[@id='txtPassword']")
# password.send_keys("admin123")
#
#
# login_btn=driver.find_element(By.XPATH,"//input[@id='btnLogin']")
# login_btn.click()
#
# Admin=driver.find_element(By.XPATH,"//b[normalize-space()='Admin']")
# Admin.click()
#
# table_row=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//tbody/tr"))
# table_clm=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']//thead/tr/th"))
# ess_count=0
# admins=[]
# print(table_row)
# for i in range(1,table_row+1):
#     xpath=f"//table[@id='resultTable']/tbody/tr[{i}]/td[3]"
#     xpath_element=driver.find_element(By.XPATH,xpath)
#     if xpath_element.text=="ESS":
#         emp_name=driver.find_element(By.XPATH,f"//table[@id='resultTable']/tbody/tr[{i}]/td[4]")
#         print(emp_name.text,xpath_element.text)
#         ess_count=ess_count+1
#     elif xpath_element.text=="Admin":
#         admins.append(xpath_element.text)
#     else:print("otherrrrrrrr")
#
# print("ess employees",ess_count)
# print("admin employees",len(admins))
# driver.quit()

             #Date
from selenium import webdriver
import time



driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
date.click()
time.sleep(2)
month="March"
day=20
year=2030


month1=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']")
year1=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']")
if month1=="June":
    print("true")
else:
    #next_btn=driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']")

    for i in range(2):

        next_btn = driver.find_element(By.XPATH, "// *[ @ id = 'ui-datepicker-div'] / div / a[2] / span")
        next_btn.click()
        time.sleep(2)
date_select=driver.find_element(By.XPATH,"//a[normalize-space()='1']")
date_select.click()
time.sleep(3)

driver.close()



# from selenium import webdriver
# import time
#
#
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://jqueryui.com/datepicker/")
# driver.maximize_window()
#
# frame=driver.find_element(By.XPATH,"//iframe[@class='demo-frame']")
# driver.switch_to.frame(0)
# input=driver.find_element(By.XPATH,"//input[@id='datepicker']")
# input.click()
#
# time.sleep(2)
# month="January"
# day="11"
# year="2025"
#
# while True:
#     month1=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']")
#     year1=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']")
#     if month1.text==month and year1.text==year:
#         break
#     else:
#         next_1=driver.find_element(By.XPATH,"// *[ @ id = 'ui-datepicker-div'] / div / a[2] / span")
#         next_1.click()
# dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# for d in dates:
#     if d.text==day:
#         d.click()
#
# time.sleep(3)
# driver.quit()









