from instagramUserInfo import email , password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By #By kullanmak için import etmek lazım.

class Instagram:
    def __init__(self,email,password):
    
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
    
    def signIn(self,email,password):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        
        emailInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
        passwordInput = self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input') 
        
        
        
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(60)
        
        
instgrm = Instagram(email,password)
instgrm.signIn(email, password)

       
       