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
            print("the user is logged in successfully\n")

    def admin_modules(self):

        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click() 
           #1st way to check menu is visible or not
           #ADMIN
           adminmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().admin)))
           if adminmodule:
               print("Admin menu is visible")
               adminmodule.click()
           print("ADMIN VALIDATED")
           print("****************")
           #2nd way to check menu is visible or not
           #PIM
           if (WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().pim)))):
                print("Pim is visible")
                self.driver.find_element(by=By.XPATH,value=location.Location().pim).click() 
           print('PIM VALIDATED')
           print("****************")
           #3rd way to check menu is visible or not
           #LEAVE
           leavemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().leave)))
           if leavemodule.is_displayed():
                print("leave menu is visible")
                leavemodule.click()
           print('LEAVE VALIDATED')
           print("****************")
           #4th way to check menu is visible or not
           #TIME
           timemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().time)))
           timemodule.click()
           print("Time menu is visible")
           print('TIME VALIDATED')
           print("****************")
           #RECRUITMENT 
           recruit_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().recruitment)))
           if recruit_module.is_displayed():
               print("recruitment menu is displayed")
               recruit_module.click()
           print('RECRUITMENT VALIDATED')
           print("****************")
           #5th way to check menu is visible or not
           #MYINFO
           myinfomodule = self.driver.find_element(by=By.XPATH,value=location.Location().myinfo)
           print("Myinfo menu is visible")
           myinfomodule.click()
           print('MYINFO VALIDATED')
           print("****************")
           #6th way to check menu is visible or not
           #PERFORMANCE
           if(self.driver.find_element(by=By.XPATH,value=location.Location().performance)):
              print("Performance menu is visible")
              self.driver.find_element(by=By.XPATH,value=location.Location().performance).click()
           print('PERFORMANCE VALIDATED')
           print("****************")
           #7th way to check menu is visible or not
           #DASHBOARD
           dashboardmodule = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, location.Location().dashboard)))
           if dashboardmodule:
               print("Dashboard menu is visible")
               dashboardmodule.click()
           print('DASHBOARD VALIDATED')
           print("****************")
           #DIRECTORY
           directorymodule = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, location.Location().directory)))
           if directorymodule:
              print("Directory menu is visible")
              directorymodule.click()
           print('DIRECTORY VALIDATED')
           print("****************")
           #MAINTENANCE
           maintenancemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().maintenance)))
           print("Maintenance menu is visible")
           maintenancemodule.click()
           self.driver.find_element(by=By.XPATH,value=location.Location().cancel).click() 
           print('MAINTENANCE VALIDATED')
           print("****************")
           #CLAIM
           claimmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().claim)))
           print("claim menu is visible")
           claimmodule.click()
           print('CLAIM VALIDATED')
           print("****************")
           #8th method to check menu is visible or not
           #BUZZ
           buzzmodule = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, location.Location().buzz)))
           print("Buzz menu is visible")
           buzzmodule.click()
           print('BUZZ VALIDATED')
           print("****************")

           print("All modules menu validated successfully")
 
    #shutdown
    def shutdown(self):
        self.driver.quit()

#object1 : 
orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.admin_modules()
orangehrm.shutdown()



