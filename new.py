# from selenium import webdriver
# import time
# # method 1
# from selenium.webdriver.chrome.service import Service
# serv_obj=Service("C:\python\seldemo\chromedriver.exe")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://www.google.com")
# time.sleep(3)
# driver.close()

#method 2
# driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# time.sleep(3)
# driver.close()



# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# time.sleep(2)
#
# search_box=driver.find_element(by=By.NAME,value="q")
# search_box.send_keys("techolas")
# time.sleep(2)
#
# search_button=driver.find_element(by=By.NAME,value="btnK")
# search_button.click()
# time.sleep(2)
# driver.close()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
#
# driver=webdriver.Chrome()
# driver.get("https://techolas.com/")
# driver.maximize_window()
# time.sleep(2)
#
#
# cousre_select=driver.find_element(by=By.CLASS_NAME,value="tc-menu-inner")
# cousre_select.click()

# search_icon=driver.find_element(by=By.CSS_SELECTOR,value='div[class="thim-widget-courses-searching template-courses-searching"]')
# search_icon.click()
# time.sleep(2)
#
# search_box=driver.find_element(by=By.NAME,value="s")
# search_box.send_keys("software testing")
# time.sleep(2)
#
# search_button=driver.find_element(by=By.CSS_SELECTOR,value='button[type="submit"]')
# search_button.click()
# time.sleep(2)
# driver.close()






