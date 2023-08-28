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

    def test_qualification_skill(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

           #4.QUALIFICATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().qualifications).click()
           #skills in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skills).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skilladd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skill_input).send_keys(info.Info().skill)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skillsave).click() 
           assert self.driver.current_url =='https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSkills'

    def test_qualification_education(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

           #4.QUALIFICATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().qualifications).click()

           #education in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().education).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().eduadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().eduinput).send_keys(info.Info().education)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().edusave).click() 
           assert self.driver.current_url =='https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewEducation' 

  

    def test_qualification_license(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

           #4.QUALIFICATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().qualifications).click()  
           #license in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licenses).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licenadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().liceninput).send_keys(info.Info().licence)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licensave).click()  
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLicenses'
  
    def test_qualification_languages(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

           #4.QUALIFICATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().qualifications).click()     
           #languages in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().languages).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langinput).send_keys(info.Info().language)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langsave).click()  
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewLanguages'
  
    def test_qualification_memberships(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

           #4.QUALIFICATION
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().qualifications).click()
          
           #memberships in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memberships).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().meminput).send_keys(info.Info().licence)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memsave).click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/membership'
           print("qualification list are validated successfully")

