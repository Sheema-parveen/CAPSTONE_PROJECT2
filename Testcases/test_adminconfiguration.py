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

    def test_email_configuration(self,startup):
         
         if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #7.CONFIGURATION
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #email configuration in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().email_config).click() 
           email=self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().mail_input)
           action = ActionChains(self.driver)
           action.click(on_element=email).perform()
           email.send_keys(Keys.CONTROL+'A')
           email.send_keys(Keys.BACK_SPACE)
           email.send_keys(info.Info().mail)

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().sendmail).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().testcheck).click() 
           self.driver.find_element(by=By.XPATH,value=adminloc.Adminlocation().testmail).send_keys(info.Info().mail)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().reset).click() 
           self.driver.find_element(by=By.XPATH,value=adminloc.Adminlocation().testmail).send_keys(info.Info().mail)
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().mailsave).click() 
           print('email configuration validated')

    def test_email_subscription(self,startup):  
          
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #email subscription  in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().email_subscription).click()  
           #selectingcheckbox
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveapplication).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leavecancellation).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveassignment).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveapproval).click() 
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leave_rejection).click()   
           print('email subscription validated')

    def test_localization(self,startup):
              
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
   
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().configuration).click() 
           #localization  in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().localization).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().loclanguageinput).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().loclanguage).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().dateformatinput).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().dateformat).click()  
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().localsave).click() 
           print('localization validated')

    def test_language_packages(self,startup):   
           
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
      
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().configuration).click() 
           #language packages in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().language_packages).click() 
           assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/admin/languagePackage' 
           print('languagepackages validated')
           """
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().packadd).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().namedrop).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().arabic).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().packsave).click()  
           """

    def test_modules(self,startup):
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
      
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #modules in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().modules).click()  
           #admin
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().admincheck).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().admincheck).click()  
           #pim
           pim= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().pimcheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=pim).perform()
           #leave
           leave= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().leavecheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=leave).perform()
           #time
           time= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().timecheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=time).perform()
           #recruitment
           recruit= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().recruitcheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=recruit).perform()
           #performance
           performance= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().performcheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=performance).perform()
           #directory
           directory= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().directorycheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=directory).perform()
           #maintainance
           maintain= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().maintaincheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=maintain).perform()
           #mobile
           mobile= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().mobilecheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=mobile).perform()
           #claim
           claim= self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().claimcheck)
           action = ActionChains(self.driver)
           action.double_click(on_element=claim).perform()
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().modulesave).click()  
           print('modules validated')

    def test_socialmedia(self,startup): 
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
         
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #social media authentication in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().social_media).click() 
           assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/admin/openIdProvider' 
           print('socialmedia authentication validated')

    def test_register_oauth(self,startup):
           
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
    
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #register oauth in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().register_oauth).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regadd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().reginput).send_keys(info.Info().nameredirect)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regurl).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regurl).send_keys(info.Info().redirect)  
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regsave).click()
           print('register oauth client validated')

    def test_ldap(self,startup):  

        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
      
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #LDAP configuration in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().ldapconfig).click()
           assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/admin/ldapConfiguration'
           print('LDAP configuration validated')
           print("configuration list are  validated successfully")
           
      



    
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         
         







