# import time
# import  requests
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
#
# page_links=driver.find_elements(By.TAG_NAME,"a")
# for link in page_links:
#     url=link.get_attribute("href")
#
#     if url.startswith("https:/"):
#      try:
#         res=requests.head(url)
#         if res.status_code>=400:
#             print("broken link",url)
#      except:
#          None
#
# time.sleep(2)
# driver.quit()


from selenium import webdriver
import time
import requests
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://techolas.com/")
driver.maximize_window()

page_links=driver.find_elements(By.TAG_NAME,"a")
for link in page_links:
    url=link.get_attribute("href")

    if url.startswith("https:/"):
        try:
            res=requests.head(url)
            if res.status_code>=400
