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

    def admin_qualification(self):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
    
           #4.QUALIFICATION
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().qualifications))).click()
           #skills in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skills).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skilladd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skill_input).send_keys(info.Info().skill)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().skillsave).click()  
           print("skill validated")

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().qualifications))).click()
           #education in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().education).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().eduadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().eduinput).send_keys(info.Info().education)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().edusave).click()  
           print("education validated")

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().qualifications))).click()
           #license in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licenses).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licenadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().liceninput).send_keys(info.Info().licence)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().licensave).click()  
           print("license validated")
  
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().qualifications))).click()
           #languages in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().languages).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langinput).send_keys(info.Info().language)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().langsave).click()
           print("languages validated")  
  

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().qualifications))).click()
           #memberships in qualification
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memberships).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().meminput).send_keys(info.Info().licence)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().memsave).click()  
           print("membership validated")
           print("qualification list are validated successfully")

    #shutdown
    def shutdown(self):
        self.driver.quit()

orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.admin_qualification()  
orangehrm.shutdown()   