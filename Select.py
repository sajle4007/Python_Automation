from selenium import webdriver
import time
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
driver.maximize_window()
country=driver.find_element(By.XPATH,"//select[@id='Form_submitForm_Country']")
country_list=Select(country)

country_list.select_by_value("India")
              #OR
 # country_list.select_by_visible_text("Algeria")


time.sleep(5)

# driver.quit()


                                            #OR
# from selenium import webdriver
# import time
# from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/?")
# driver.maximize_window()
# country=driver.find_element(By.XPATH,"//select[@id='Form_submitForm_Country']")
# country_list=Select(country)
#
# options=driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']//option")
# # print(len(options))
#
# for op in options:
#     if op.get_attribute("value")=="India":
#         op.click()
# time.sleep(5)
# driver.quit()




