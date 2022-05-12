# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\python\seldemo\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.bmw.com")
# time.sleep(2)
# driver.close()

# driver=webdriver.Chrome()
# driver.get("https://www.bmw.com")
# time.sleep(2)
# driver.close()


#OrangeHRM

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# Actual_title="OrangeHRM"
# Admin_username="Admin"
# Admin_password="admin123"
# driver=webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# time.sleep(2)
#
# username=driver.find_element(by=By.NAME,value="txtUsername")
# password=driver.find_element(by=By.NAME,value="txtPassword")
# time.sleep(1)
#
# username.send_keys(Admin_username)
# time.sleep(1)
# password.send_keys(Admin_password)
# time.sleep(1)
#
# login_btn=driver.find_element(by=By.NAME,value="Submit")
# login_btn.click()
# time.sleep(1)
#
# a=driver.find_element(by=By.LINK_TEXT,value="Welcome Paul")
# a.click()
# time.sleep(2)
#
#
# captured_title=driver.title
# if captured_title==Actual_title:
#     print("Test passed")
# else:
#     print("Test failed")
# driver.close()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# # actual_name="viewport"
# admin_username=
# admin_password=
# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com/")
# driver.maximize_window()
# time.sleep(2)
#
# username=driver.find_element(by=By.NAME,value="email")
# time.sleep(1)
# password=driver.find_element(by=By.NAME,value="pass")
# time.sleep(1)
#
# username.send_keys(admin_username)
# time.sleep(2)
# password.send_keys(admin_password)
# time.sleep(2)
#
# login_button=driver.find_element(by=By.NAME,value="login")
# login_button.click()

# captured_name=driver.name
# if captured_name==actual_name:
#     print("pass")
# else:
#     print("fail")
# driver.close()

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://www.bmw.in/")
driver.maximize_window()

print("title: ",driver.title)
print("website url: ",driver.current_url)
print("resources: ",driver.page_source)

driver.quit()











