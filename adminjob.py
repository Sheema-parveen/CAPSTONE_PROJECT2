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

    def admin_job(self):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
         
           #2.JOB
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
            
           #WebDriverWait(self.driver, 10) .until(EC.presence_of_element_located((By.XPATH, location.Location().admin))).click()
           #2.JOB
           #WebDriverWait(self.driver, 10) .until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().job))).click()
           
           #job_title in job
           jobtitle = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().job_title)
           action = ActionChains(self.driver)
           action.click(on_element=jobtitle).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_title ).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_titleedit ).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_title_input ).click()
           self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().job_title_input).send_keys(info.Info().job_titleinput)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savetitle).click()
           print("jobtitle validated")
           
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().job))).click()
       
           #pay grade in job 
           paygrade = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().pay_grades)
           action = ActionChains(self.driver)
           action.click(on_element=paygrade).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().pay_grades).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().payadd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().pay_name).send_keys(info.Info().payname)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savepay).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().paycuradd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().curencyinput).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().rupees).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savecurrency).click() 
           print("paygrade validated")
           
           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().job))).click()
       
           #employment status in job 
           empstatus = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().employment_status)
           action = ActionChains(self.driver)
           action.click(on_element=empstatus).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().employment_status).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().addemp).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().emp_input).send_keys(info.Info().empstatus)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().empsave).click()  
           print("employmentstatus validated")

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().job))).click()
       
           #job categories in job 
           jobcategory = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().job_categories)
           action = ActionChains(self.driver)
           action.click(on_element=jobcategory).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_categories).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().catadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().categoryinput).send_keys(info.Info().category)  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().catsave).click()
           print("job category validated")

           WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, adminloc.Adminlocation().job))).click()
       
           #workshifts in job 
           workshift = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().workshifts)
           action = ActionChains(self.driver)
           action.click(on_element=workshift).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().workshifts).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().workadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().shiftinput).send_keys(info.Info().shift)  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().shiftsave).click()
           print("workshift validated")
           print(" job menu list are validated successfully")
       
    #shutdown
    def shutdown(self):
        self.driver.quit()

orangehrm = Orangehrm(info.Info().url)
orangehrm.login()
orangehrm.admin_job()
orangehrm.shutdown()