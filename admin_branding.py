from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from Test_Information import info
from Test_Location import location
from Test_Location import adminloc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

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

    def admin_corporate(self):
           
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
           print(buttoncolor1)

           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().publish).click()
           sleep(3)

           after_publish=self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().publish)
           buttoncolor2=after_publish.value_of_css_property('color')
           print(buttoncolor2)
           if(buttoncolor1!=buttoncolor2):
                 print("corporate branding validated successfully")

                   
    #shutdown
    def shutdown(self):
        self.driver.quit()

orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.admin_corporate()
orangehrm.shutdown()    
           
           
           
           
           
           
           
          
