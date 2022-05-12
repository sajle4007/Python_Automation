# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\python\seldemo\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.google.com")
# time.sleep(3)
# driver.close()


#Assignment
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
actual_title="Dashboard / nopCommerce administration"
Admin_email="admin@yourstore.com"
Admin_password="admin"
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)

username=driver.find_element(by=By.ID,value="Email")
password=driver.find_element(by=By.ID,value="Password")
username.clear()
password.clear()
time.sleep(2)

username.send_keys(Admin_email)
time.sleep(1)
password.send_keys(Admin_password)
time.sleep(1)

login_btn=driver.find_element(by=By.CSS_SELECTOR,value='button[type="submit"]')
login_btn.click()
actual_tittle="Dashboard / nopCommerce administration"
captured_title=driver.title
if(captured_title==actual_tittle):
    print("test passed")
else:
    print("test failed")

driver.close()

#Assignment problem by using css selectors
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
admin_email="admin@yourstore.com"
admin_password="admin"
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(1)

username=driver.find_element(by=By.CSS_SELECTOR,value="input#Email")
password=driver.find_element(by=By.CSS_SELECTOR,value="input.password")
username.clear()
password.clear()
time.sleep(1)

username.send_keys(admin_email)
password.send_keys(admin_password)
time.sleep(2)

# login_btn=driver.find_element(by=By.CSS_SELECTOR,value='button[type=submit]')
        #OR
login_btn=driver.find_element(by=By.CSS_SELECTOR,value="button.button-1[type=submit]")
login_btn.click()
time.sleep(2)

driver.close()

#techolas site automation
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://techolas.com/")
# driver.maximize_window()
# time.sleep(1)
#
# search_icon=driver.find_element(by=By.XPATH,value="//li[@class='menu-right']//div[@class='thim-widget-courses-searching template-courses-searching']")
# search_icon.click()
#
# search_box=driver.find_element(by=By.XPATH,value="//li[@class='menu-right']//input[@placeholder='Search courses...']")
# search_box.send_keys("software testing")
# time.sleep(1)
#
# course_select=driver.find_element(by=By.XPATH,value="//a[@class='ui-corner-all']")
# course_select.click()



# course_list=driver.find_element(by=By.CSS_SELECTOR,value="a.tc")
# course_list.click()
# time.sleep(2)
#
# course_select=driver.find_element(by=By.CSS_SELECTOR,value="a[href=https://techolas.com/course/software-testing/]")
# course_select.click()
# time.sleep(1)
# driver.close()









