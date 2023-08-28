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
from selenium.webdriver.common.keys import Keys

#Test_suite
class Test_project:  
    # Boot method to run Pytest using POM
    @pytest.fixture
    def startup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))        
        yield
        self.driver.close()

    def test_get_title(self,startup):
        self.driver.get(info.Info().url)
        assert self.driver.title=="OrangeHRM"
        print("success:correct url")
   
    # valid login testing
    def test_login1(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.NAME, value=location.Location().username_input_box).send_keys(info.Info().Username)
        self.driver.find_element(by=By.NAME, value=location.Location().password_input_box).send_keys(info.Info().password)
        self.driver.find_element(by=By.XPATH, value=location.Location().submit_button).click()
        assert self.driver.title == 'OrangeHRM'
        print("the user is logged in successfully")

    def test_usermanagement(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            #1.USERMANAGEMENT
           usermanagement = WebDriverWait(self.driver, 10) .until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().user_management)))
           usermanagement.click()
           self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().users).click()
           self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().useredit).click()
           assert self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().usersave).click()
           print("usermanagement validated successfully")

           