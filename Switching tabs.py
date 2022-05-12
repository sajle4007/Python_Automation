                                 #popup window
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# click_button=driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']")
# click_button.click()
#
# alert_w=driver.switch_to.alert
# time.sleep(2)
#
# print(alert_w.text)
# alert_w.send_keys("sfsdds0")
# time.sleep(2)
# alert_w.dismiss()
#
# driver.quit()

                                         #Frames
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()
# driver.switch_to.frame("packageListFrame")
# window_1=driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium.chrome']")
# window_1.click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("packageFrame")
# window_2=driver.find_element(By.XPATH,"//a[normalize-space()='ChromeDriver']")
# window_2.click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("classFrame")
# window_3=driver.find_element(By.XPATH,"//header[@role='banner']//ul[1]//li[3]//a[1]")
# window_3.click()
# time.sleep(2)
# driver.close()

#                                        #OR
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
# driver.maximize_window()
# window_1=driver.find_element(By.XPATH,"//iframe[@title='All Packages']")         #by using xpath instead of name
# driver.switch_to.frame(window_1)
#
# window_1=driver.find_element(By.XPATH,"//a[normalize-space()='org.openqa.selenium.chrome']")
# window_1.click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("packageFrame")
# window_2=driver.find_element(By.XPATH,"//a[normalize-space()='ChromeDriver']")
# window_2.click()
# time.sleep(2)
# driver.switch_to.default_content()
#
# driver.switch_to.frame("classFrame")
# window_3=driver.find_element(By.XPATH,"//header[@role='banner']//ul[1]//li[3]//a[1]")
# window_3.click()
# time.sleep(2)
# driver.close()


                       #SWITCHING B/W TABS(browser windows)
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# time.sleep(2)
#
# click_btn=driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
# click_btn.click()
#
# window_ids=driver.window_handles
# driver.switch_to.window(window_ids[1])
#
# free_trial=driver.find_element(By.XPATH,"//input[@id='linkadd']")
# free_trial.click()
#
# driver.switch_to.window(window_ids[0])
# time.sleep(2)
#
# driver.quit()



# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.maximize_window()
# time.sleep(2)
#
# c_btn1=driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']")
# for i in range(4):
#     time.sleep(1)
#     c_btn1.click()
# time.sleep(2)
# window_ids=driver.window_handles
#
# driver.switch_to.window(window_ids[3])
# time.sleep(1)
# driver.close()
# driver.switch_to.window(window_ids[2])
# time.sleep(1)
# driver.close()
# driver.switch_to.window(window_ids[1])
# time.sleep(1)
# driver.close()
# driver.switch_to.window(window_ids[0])
# time.sleep(1)
#
# driver.quit()


                                 #slide 55 problem
# from selenium import webdriver
# import time
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# time.sleep(2)
#
# click_me=driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']")
# click_me.click()
#
# alert_w=driver.switch_to.alert
# alert_w.dismiss()
#
# time.sleep(3)
#
#
# search_box=driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']")
# search_box.send_keys("tesing")
# submit_btn=driver.find_element(By.XPATH,"//input[@type='submit']")
# submit_btn.click()
# time.sleep(2)
#
# link1=driver.find_element(By.XPATH,"//a[normalize-space()='Testing cosmetics on animals']")
# link1.click()
# time.sleep(2)
# driver.quit()
                                    #Blocking browser popup windows

from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
opt=webdriver.ChromeOptions()
opt.add_argument("__disable_notifications__")
driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(2)
driver.quit()














