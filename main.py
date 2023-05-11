from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.page_load_strategy = 'none'

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.instagram.com/")
time.sleep(3)
driver.implicitly_wait(3)

log_in = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
log_in.send_keys("kabhi30@gmail.com")
password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys("Abhi@9881")
password.send_keys(Keys.ENTER)
time.sleep(3)
driver.implicitly_wait(3)

off_notification = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
print(off_notification.text)
off_notification.click()
time.sleep(3)

driver.get('https://www.instagram.com/fitnesstalks_with_pranit/')
time.sleep(3)
driver.implicitly_wait(5)
followers = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
followers.click()
time.sleep(2)

modal = driver.find_element(By.CSS_SELECTOR, 'div._aano')
time.sleep(5)
for i in range(10):
        #In this case we're executing some Javascript, that's what the execute_script() method does. 
        #The method can accept the script as well as a HTML element. 
        #The modal in this case, becomes the arguments[0] in the script.
        #Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
        driver.implicitly_wait(3)
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
        time.sleep(2)
print(modal.tag_name, modal.text)

# try:
#         follow_list_btns = driver.find_elements(By.CSS_SELECTOR, 'button')
#         for button in (follow_list_btns):
#                 print(button.text)
#                 if button.text == "Follow":
#                         button.click()
#                         time.sleep(2)
# # except ElementClickInterceptedException:
#         cancel_button = driver.find_element(By.XPATH,
#         '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/button')
#         cancel_button.click()

# /html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div
# /html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div # working
# /html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div 
# /html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2] 
# /html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div #working
# /html/body/div[2]/div/div[2]/div/div[2] #error copied from web
# /html/body/div[4]/div/div/div[2] # error