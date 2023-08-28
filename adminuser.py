#PROJECT2
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Location import location
from Test_Location import adminloc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Python Exception Class
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException

class Orangehrm:
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)
    
    #get title
    def get_title(self):
        self.driver.get(info.Info().url)
        self.driver.title=="OrangeHRM"
        print("success:correct url")
        
    #login1 : successful employee login to orangeHRM portal
    def login(self):
        self.driver.find_element(by=By.NAME,value=location.Location().username_input_box).send_keys(info.Info().Username)
        self.driver.find_element(by=By.NAME,value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
            print("the user is logged in successfully")

    def admin_usermanagement(self):

        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
   
        #1.USERMANAGEMENT
        usermanagement = WebDriverWait(self.driver, 10) .until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().user_management)))
        usermanagement.click()
        self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().users).click()
        self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().useredit).click()
        self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().usersave).click()
        print("usermanagement validated successfully")


    
    #shutdown
    def shutdown(self):
        self.driver.quit()

#object1 : 
orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.admin_usermanagement()
orangehrm.shutdown()


