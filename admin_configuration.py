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
from selenium.webdriver.common.keys import Keys

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

    def email_configuration(self):   

        #Admin
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
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().mailsave).click() 
           print('email configuration validated')

    def email_subscription(self):        
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #email subscription  in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().email_subscription).click()  
           #selectingcheckbox
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveapplication).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leavecancellation).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveassignment).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leave_rejection).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().leaveapproval).click()  
           print('email subscription validated')

    def localization(self):
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().configuration).click() 
           #localization  in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().localization).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().loclanguageinput).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().loclanguage).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().dateformatinput).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().dateformat).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().localsave).click() 
           print('localization validated')

    def language_packages(self):   
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().configuration).click() 
           #language packages in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().language_packages).click()  
           print('languagepackages validated')
           """
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().packadd).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().namedrop).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().arabic).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().packsave).click()  
           """

    def modules(self):
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
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().modulesave).click()  
           print('modules validated')

    def socialmedia(self): 
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #social media authentication in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().social_media).click()  
           print('socialmedia authentication validated')

    def register_oauth(self):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #register oauth in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().register_oauth).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regadd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().reginput).send_keys(info.Info().nameredirect)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regurl).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regurl).send_keys(info.Info().redirect)  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().regsave).click()
           print('register oauth client validated')

    def ldap(self):  
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().configuration))).click()
           #LDAP configuration in configuration
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().ldapconfig).click() 
           print('LDAP configuration validated')
           print("configuration list are  validated successfully")
           
    #shutdown
    def shutdown(self):
        self.driver.quit()
      


orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.email_configuration()
orangehrm.email_subscription()
orangehrm.localization()
orangehrm.language_packages()
orangehrm.modules()
orangehrm.socialmedia()
orangehrm.register_oauth()
orangehrm.ldap()
orangehrm.shutdown()


