# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://ebhorsman.com/")
# driver.maximize_window()
#
# signin_button=driver.find_element(by=By.CSS_SELECTOR,value="a.btn")
# signin_button.click()
#
# #signup_btn=driver.find_element(by=By.CSS_SELECTOR,value="div.button")
# signup_btn=driver.find_element(by=By.XPATH,value="//div[@class='button bRight pull-left']")
# signup_btn.click()
# print(driver.current_url)
# first_name=driver.find_element(by=By.XPATH,value="//input[@placeholder='First Name']")
# if first_name.is_displayed() and first_name.is_enabled():
#     first_name.send_keys("sajle")
# else:
#     print("first name is not displayed or first name is not enabled")
#
# last_name=driver.find_element(by=By.XPATH,value="//input[@placeholder='Last Name']")
# last_name.send_keys("kk")
#
# email_adress=driver.find_element(by=By.XPATH,value="//input[@placeholder='Email address']")
# email_adress.send_keys("sajle4007@gmail.com")
#
# password=driver.find_element(by=By.XPATH,value="//input[@placeholder='Password - min 5 characters']")
# password.send_keys("Work@@4007")
#
# verify_pswd=driver.find_element(by=By.XPATH,value="//input[@placeholder='Verify Password']")
# verify_pswd.send_keys("Work@@4007")
#
# customer_id=driver.find_element(by=By.XPATH,value="//input[@placeholder='Customer ID']")
# customer_id.send_keys("4444")
#
# final_signup=driver.find_element(by=By.XPATH,value="//button[normalize-space()='SignUp']")
# final_signup.click()
#
# print("title",driver.title)
# print("website url",driver.current_url)
#
# driver.close()


from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get("https://techolas.com/gallery/")
driver.maximize_window()

images=driver.find_elements(By.XPATH,"//main[@id='main']//img")
print(type(images))

for node in images:
    print("links: ",node.get_attribute("src"))

driver.quit()










#sample problem
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.bigboytoyz.com/")
# driver.maximize_window()

# navigator_tab=driver.find_element(by=By.XPATH,value="//div[@class='navtrigger']")
# navigator_tab.click()
#
# used_cars=driver.find_element(by=By.XPATH,value="//span[normalize-space()='Used Cars']")
# used_cars.click()
#
# filter_btn=driver.find_element(by=By.XPATH,value="//div[@class='filtersbtn']")
# filter_btn.click()
#
# reg_year=driver.find_element(by=By.XPATH,value="//label[normalize-space()='2015 - 2020']")
# reg_year.click()
#
# kms_driven=driver.find_element(by=By.XPATH,value="//label[normalize-space()='10000 - 15000']")
# kms_driven.click()
#
# budget=driver.find_element(by=By.XPATH,value="//label[normalize-space()='1Cr to 1.5Cr']")
# budget.click()
#
# type=driver.find_element(by=By.XPATH,value="//label[normalize-space()='SUV']")
# type.click()
#
# apply_btn=driver.find_element(by=By.XPATH,value="//button[normalize-space()='Apply Filter']")
# apply_btn.click()
#
# car_select=driver.find_element(by=By.XPATH,value="//img[contains(@alt,'Range Rover Vogue')]")
# car_select.click()
#
# home=driver.find_element(by=By.XPATH,value="//img[@class='hide-900']")
# home.click()
#
# driver.quit()

#flipkart Automated

# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.google.com")
# driver.maximize_window()
# search_input=driver.find_element(by=By.XPATH,value="//input[@title='Search']")
# search_input.send_keys("flipkart login")
# search_btn=driver.find_element(by=By.XPATH,value="//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
# search_btn.click()
# link_select=driver.find_element(by=By.XPATH,value="//h3[normalize-space()='Flipkart']")
# link_select.click()
#
# # login_btn=driver.find_element(by=By.XPATH,value="//a[normalize-space()='Login']")
# # login_btn.click()
#
# mobile_no=driver.find_element(by=By.XPATH,value="//input[@class='_2IX_2- VJZDxU']")
# mobile_no.send_keys("9895194007")
#
# password=driver.find_element(by=By.XPATH,value="//input[@type='password']")
# password.send_keys("flip##007")
#
# submit=driver.find_element(by=By.XPATH,value="//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
# submit.click()
#
# search_box=driver.find_element(by=By.XPATH,value="//input[@placeholder='Search for products, brands and more']")
# # if search_box.is_displayed() and search_box.is_enabled():
# search_box.send_keys("iphone 13 pro")
# else:
#     print("search box in not displayed or search box in not enabled")

# search_btn=driver.find_element(by=By.XPATH,value="//button[@type='submit']")
# search_btn.click()
#
# model_select=driver.find_element(by=By.XPATH,value="//div[normalize-space()='APPLE iPhone 13 Pro (Graphite, 256 GB)']")
# model_select.click()
#
# add_to_cart=driver.find_element(by=By.XPATH,value="//button[normalize-space()='ADD TO CART']")
# add_to_cart.click()
#
# remove_btn=driver.find_element(by=By.XPATH,value="//div[normalize-space()='Remove']")
# remove_btn.click()
# remove=driver.find_element(by=By.XPATH,value="//div[@class='_3dsJAO _24d-qY FhkMJZ']")
# remove.click()
#
# shop_now=driver.find_element(by=By.XPATH,value="//span[normalize-space()='Shop now']")
# shop_now.click()
#
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions
# driver=webdriver.Chrome()
# my_dt=WebDriverWait(driver,10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.google.com")
# driver.maximize_window()
#
# search_input=driver.find_element(by=By.XPATH,value="//input[@title='Search']")
# search_input.send_keys("flipkart login")
# search_btn=driver.find_element(by=By.XPATH,value="//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")
# search_btn.click()
# link_select=driver.find_element(by=By.XPATH,value="//h3[normalize-space()='Flipkart']")
# link_select.click()

# login_btn=driver.find_element(by=By.XPATH,value="//a[normalize-space()='Login']")
# login_btn.click()

# mobile_no=driver.find_element(by=By.XPATH,value="//input[@class='_2IX_2- VJZDxU']")
# mobile_no.send_keys("9895194007")
#
# password=driver.find_element(by=By.XPATH,value="//input[@type='password']")
# password.send_keys("flip##007")
#
# submit=driver.find_element(by=By.XPATH,value="//button[@class='_2KpZ6l _2HKlqd _3AWRsL']")
# submit.click()

# search_box=driver.find_element(by=By.XPATH,value="//input[@placeholder='Search for products, brands and more']")
# # if search_box.is_displayed() and search_box.is_enabled():
# search_box.send_keys("iphone 13 pro")
# else:
#     print("search box in not displayed or search box in not enabled")

# search_btn=my_dt.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[@type='submit']")))
# search_btn.click()

# mobiles_tab=driver.find_element(by=By.XPATH,value="//div[contains(@class,'xtXmba')][normalize-space()='Mobiles']")
# mobiles_tab.click()
#
# model_select=driver.find_element(by=By.XPATH,value="//body[1]/div[1]/div[1]/div[3]/div[8]/div[1]/a[1]/div[1]/div[1]/img[2]")
# model_select.click()
#
#model=driver.find_element(by=By.XPATH,value="//div[normalize-space()='APPLE iPhone 12 (Black, 128 GB)']")
# model.click()
#
# add_to_cart=driver.find_element(by=By.XPATH,value="//button[normalize-space()='ADD TO CART']")
# add_to_cart.click()
#
# remove_btn=driver.find_element(by=By.XPATH,value="//div[normalize-space()='Remove']")
# remove_btn.click()
# remove=driver.find_element(by=By.XPATH,value="//div[@class='_3dsJAO _24d-qY FhkMJZ']")
# remove.click()
#
# shop_now=driver.find_element(by=By.XPATH,value="//span[normalize-space()='Shop now']")
# shop_now.click()
#
# driver.quit()


#Amazon automated
# from selenium import webdriver
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://www.amazon.in/Apple-iPhone-13-Pro-128GB/dp/B09G91LWTZ/ref=sr_1_5?crid=15AC8EEOEW81N&keywords=iphone%2B13%2Bpro&qid=1650904442&sprefix=i%2Caps%2C2103&sr=8-5&th=1")
# driver.maximize_window()
# google_search_box=driver.find_element(by=By.XPATH,value="//input[@title='Search']")
# google_search_box.send_keys("amazon.in")
#
# google_search_btn=driver.find_element(by=By.XPATH,value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]")
#
#
# link_select=driver.find_element(by=By.XPATH,value="//h3[normalize-space()='Amazon.in']")
# link_select.click()
#
# search_box=driver.find_element(by=By.XPATH,value="//input[@id='twotabsearchtextbox']")
# if search_box.is_displayed() and search_box.is_enabled():
#     search_box.send_keys("iphone 13 pro")
# else:
#     print("search box in not displayed or search box in not enabled")
#
# search_btn=driver.find_element(by=By.XPATH,value="//input[@id='nav-search-submit-button']")
# search_btn.click()
#
# model_select=driver.find_element(by=By.XPATH,value="//span[@class='a-size-medium a-color-base a-text-normal'][normalize-space()='Apple iPhone 13 Pro (128GB) - Graphite']")
# model_select.click()
#
# window_ids=driver.window_handles
# driver.switch_to.window(window_ids[1])




# add_to_cart=driver.find_element(By.ID,"add-to-cart-button")
# add_to_cart.click()
#
# go_to_cart=driver.find_element(by=By.XPATH,value="//a[normalize-space()='Go to Cart']")
# go_to_cart.click()
#
# delete_item=driver.find_element(By.NAME,"submit.delete.Cd46d1206-d49d-4c88-85e5-f1c4b4782598")
# delete_item.click()
#
# home=driver.find_element(by=By.XPATH,value="//a[@id='nav-logo-sprites']")
# home.click()
#
# driver.quit()



# from selenium import webdriver
# import time
# # from selenium.webdriver.support.select import Select
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# from selenium.webdriver.common.by import By
# driver.get("https://techolas.com/")
# driver.maximize_window()
#
# search_icon=driver.find_element(By.XPATH,"//li[@class='menu-right']//div[@class='thim-widget-courses-searching template-courses-searching']")
# search_icon.click()
#
# search_box=driver.find_element(By.XPATH,"//li[@class='menu-right']//input[@placeholder='Search courses...']")
# search_box.send_keys("software testing")
#
# submit=driver.find_element(By.XPATH,"//li[@class='menu-right']//button[@type='submit']")
# submit.click()
# time.sleep(1)
# # course_list=Select(search_box)
# # course_list.select_by_value("Software Testing")
# time.sleep(1)
#
# driver.quit()



