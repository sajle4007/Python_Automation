#To print multiple links
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.orangehrm.com/")
driver.maximize_window()
time.sleep(2)

centre_area_images=driver.find_elements(by=By.XPATH,value="//div[@class='container-fluid logos-block']//img")
print(type(centre_area_images))

for node in centre_area_images:
    print("link :",node.get_attribute("src"))

time.sleep(2)

driver.close()



#To print the all link contained in the given webpage
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# links=driver.find_elements(by=By.TAG_NAME,value="a")
# print(len(links))
# driver.close()



#To print the footer area links in the given website
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# footer_area_links=driver.find_elements(by=By.XPATH,value="//div[@class='footer__bottom']//a")
# print(type(footer_area_links))
#
# for node in footer_area_links:
#     print("link:",node.get_attribute("href"))
# driver.close()


#To print the text in a particular area in the given website
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# achievements=driver.find_elements(by=By.XPATH,value="//div[@class='footer__top']//div")
# print(len(achievements))
# for node in achievements:
#     print("Texts:",node.get_attribute("class"))
# driver.close()



#Locating using class_name

# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(1)
#
# List_elements=driver.find_elements(by=By.CLASS_NAME,value="col-xs-12")
# # print(len(List_elements))
#
#
#
# for node in List_elements:
#     print("classes:",node.get_attribute("class"))
#
# driver.close()


