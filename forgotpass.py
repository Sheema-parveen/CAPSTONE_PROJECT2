#PROJECT2
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Location import location
from selenium.webdriver.common.by import By
from time import sleep

class Orangehrm:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
    #FORGOT PASSWORD
    def forgot(self):
        self.driver.find_element(by=By.XPATH,value=location.Location().forgot_password).click()
        self.driver.find_element(by=By.NAME,value=location.Location().Username_inputbox).send_keys(info.Info().Username)
        self.driver.find_element(by=By.XPATH, value=location.Location().reset_button).click()
        sleep(3)
        print("Reset password link sent successfully")

    #shutdown
    def shutdown(self):
        self.driver.quit()

#object1 : RESET PASSWORD
orangehrm = Orangehrm(info.Info().url)
orangehrm.forgot()
orangehrm.shutdown()