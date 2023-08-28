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
from selenium.webdriver.common.keys import Keys
from time import sleep

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

    def test_admin_corporate_branding(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()

             
           #6.CORPORATE BRANDING
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().corporate_branding))).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().primarycolor).click()
           el=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().primary_input) 
           action = ActionChains(self.driver)
           action.click(on_element=el).perform()
           el.send_keys(Keys.CONTROL+'A')
           el.send_keys(Keys.BACK_SPACE)
           el.send_keys(info.Info().pc)
           print("primary color changed")
           
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().secondarycolor).click()
           el1=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().secondary_input)
           action = ActionChains(self.driver)
           action.click(on_element=el1).perform()
           el1.send_keys(Keys.CONTROL+'A')
           el1.send_keys(Keys.BACK_SPACE)
           el1.send_keys(info.Info().sc)
           print("secondary color changed")

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().primaryfontcolor).click()
           f1=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().font_input1)
           action = ActionChains(self.driver)
           action.click(on_element=f1).perform()
           f1.send_keys(Keys.CONTROL+'A')
           f1.send_keys(Keys.BACK_SPACE)
           f1.send_keys(info.Info().font1)
           print("primary font color changed")

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().secondaryfontcolor).click()
           f2=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().font_input2)
           action = ActionChains(self.driver)
           action.click(on_element=f2).perform()
           f2.send_keys(Keys.CONTROL+'A')
           f2.send_keys(Keys.BACK_SPACE)
           f2.send_keys(info.Info().sc)
           print("secondary font color changed")


           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().gradient1).click()
           el2=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().gradient_input)
           action = ActionChains(self.driver)
           action.click(on_element=el2).perform()
           el2.send_keys(Keys.CONTROL+'A')
           el2.send_keys(Keys.BACK_SPACE)
           el2.send_keys(info.Info().pg1)
           print("primary gradient color1  changed")

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().gradient2).click()
           el3=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().grad_input)
           action = ActionChains(self.driver)
           action.click(on_element=el3).perform()
           el3.send_keys(Keys.CONTROL+'A')
           el3.send_keys(Keys.BACK_SPACE)
           el3.send_keys(info.Info().pg2)
           print("primary gradient color2  changed")

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().socialcheck).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().preview).click()
           before_publish=self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().publish)
           buttoncolor1=before_publish.value_of_css_property('color')

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().publish).click()
           sleep(3)
           after_publish=self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().publish)
           buttoncolor2=after_publish.value_of_css_property('color')

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().default).click()
           assert buttoncolor1!=buttoncolor2
           print("corporate branding validated successfully")