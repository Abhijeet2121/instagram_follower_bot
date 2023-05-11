# class InstaFollower:
#     def __init__(self):
#         self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
#         self.driver.get("https://www.instagram.com/")
#         time.sleep(3)

#     def login(self):
#         self.log_in = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
#         self.log_in.send_keys("kabhi30@gmail.com")
#         self.password = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
#         self.password.send_keys("Abhi@9881")
#         self.password.send_keys(Keys.ENTER)
#         time.sleep(5)
#         self.driver.implicitly_wait(10)

#         off_notification = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
#         print(off_notification.text)
#         off_notification.click()

#     def find_followers(self):
#         self.driver.get('https://www.instagram.com/fitnesstalks_with_pranit/')
#         time.sleep(2)
#         followers = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_Xa"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')
#         followers.click()
#     def follow(self):
#         pass

# bot = InstaFollower()
# bot.login()
# bot.find_followers()
# bot.follow()