# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.google.com")
# driver.maximize_window()
# time.sleep(2)
#
# img=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[2]/div/img")
# img.click()
# driver.close()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome()
# driver.get("https://www.orangehrm.com/")
# driver.maximize_window()
# time.sleep(2)
#
# company_tab=driver.find_element(by=By.XPATH,value="//a[@class='link'][normalize-space()='Company']")
# company_tab.click()
# time.sleep(1)
#
# career_link=driver.find_element(by=By.XPATH,value="//a[@href='company/careers/current-vacancies/']")
# career_link.click()
# time.sleep(1)
# driver.close()

                                # To print multiple links

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

# footer_area_links=driver.find_elements(by=By.XPATH,value=")