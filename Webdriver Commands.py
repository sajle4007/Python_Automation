                                          #Get commands

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")      #get() is a webdriver command......!!!!!!!
# driver.maximize_window()
# time.sleep(2)
#
# print("title",driver.title)
# print("website adress",driver.current_url)
# print("page resource code",driver.page_source)
#
# driver.close()

                                            #Conditional commands
#is_displayed()  & is_enabled()

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/hris-hr-software-demo/")
# driver.maximize_window()
# time.sleep(2)
#
# first_name=driver.find_element(by=By.XPATH,value="//input[@id='Form_submitForm_FirstName']")
# if first_name.is_displayed() and first_name.is_enabled():
#     first_name.send_keys("gggggg")
# else:
#     print("failed,first name not displayed or first name not enabled")
# time.sleep(2)
# driver.close()

#is_selected()
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://admin-demo.nopcommerce.com/")
# driver.maximize_window()
# time.sleep(2)
#
# check_box=driver.find_element(By.XPATH,"//input[@id='RememberMe']")
# print("default status",check_box.is_selected())
# time.sleep(2)
# check_box.click()
# time.sleep(2)
# print("status after click",check_box.is_selected())
# driver.quit()




                                      #Browser Commands
#Quit()
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# # free_trial=driver.find_element(by=By.XPATH,value="//input[@id='linkadd']")
# # free_trial.click()
# privacy_button=driver.find_element(by=By.XPATH,value="//a[normalize-space()='Privacy Policy']")
# time.sleep(5)
# privacy_button.click()
# driver.quit()


                                   #Navigation commands

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# driver.get("https:www.amazon.in")
# time.sleep(2)
# driver.back()
# time.sleep(1)
# driver.forward()
# time.sleep(1)
# driver.refresh()
# time.sleep(1)
# driver.quit()


                              #Wait Commands
#implicitly_wait()

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
#
# free_trial=driver.find_element(by=By.XPATH,value="//input[@id='linkadd']")
# free_trial.click()
# driver.quit()

#Explicitly_wait()

# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver=webdriver.Chrome()
# my_dt=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
# from selenium.webdriver.common.by import By
# driver.get("https://www.orangehrm.com")
# driver.maximize_window()
#
# free_trial_button=my_dt.until(expected_conditions.element_to_be_clickable((By.XPATH,"//input[@id='linkadd']")))
# free_trial_button.click()
# driver.quit()

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver=webdriver.Chrome()
my_dt=WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
from selenium.webdriver.common.by import By
driver.get("https://www.orangehrm.com")
driver.maximize_window()

fr_tr=driver.find_element(By.XPATH,"//input[@id='linkadd']")
fr_tr.click()
driver.quit()

