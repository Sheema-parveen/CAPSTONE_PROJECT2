from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Information import info
from Test_Location import location
from Test_Location import adminloc
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#Test_suite
class Test_project:  
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))        
        yield
        self.driver.close()
   
    # valid login testing
    def test_login1(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=location.Location().username_input_box).send_keys(info.Info().Username)
        self.driver.find_element(by=By.NAME, value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        assert self.driver.title == 'OrangeHRM'
        print("the user is logged in successfully")
    
    def test_general_info(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
           #3.ORGANIZATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().organization).click()
           #general information in organization
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().general_info).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().editcheck).click()  
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().infosave).click()  

    def test_location(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
           #3.ORGANIZATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().organization).click()
           #location in organization
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().location).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().locadd).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().locname_input).send_keys(info.Info().place)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().loccountry).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().india).click() 
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().locsave).click() 

    def test_structure(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
           #3.ORGANIZATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().organization).click()
           #structure in organization
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().structure).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().strucedit).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().strucadd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().strucname_input).send_keys(info.Info().structname) 
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().structsave).click() 

           print("organization menu list are validated successfully")
