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

    def test_admin_job(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #2.JOB
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
        
           #job_title in job
           jobtitle = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().job_title)
           action = ActionChains(self.driver)
           action.click(on_element=jobtitle).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_title ).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_titleedit ).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_title_input ).click()
           self.driver.find_element(by=By.XPATH,value= adminloc.Adminlocation().job_title_input).send_keys(info.Info().job_titleinput)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savetitle).click()
           assert self.driver.current_url==' https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveJobTitle'

    def test_paygrade(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #2.JOB
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
           
           #pay grade in job 
           paygrade = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().pay_grades)
           action = ActionChains(self.driver)
           action.click(on_element=paygrade).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().pay_grades).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().payadd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().pay_name).send_keys(info.Info().payname)
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savepay).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().paycuradd).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().rupees).click() 
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().savecurrency).click() 
           
    def test_employment(self,startup):
        #Admin
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #2.JOB
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
           #employment status in job 
           empstatus = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().employment_status)
           action = ActionChains(self.driver)
           action.click(on_element=empstatus).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().employment_status).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().addemp).click()  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().emp_input).send_keys(info.Info().empstatus)
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().empsave).click()  

    def test_jobcategory(self,startup): 
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #2.JOB       
           #job categories in job 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
           jobcategory = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().job_categories)
           action = ActionChains(self.driver)
           action.click(on_element=jobcategory).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job_categories).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().catadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().categoryinput).send_keys(info.Info().category)  
           assert self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().catsave).click()
           

    def test_workshift(self,startup): 
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
           #2.JOB  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().job).click()
           #workshifts in job
           workshift = self.driver.find_element(by=By.XPATH, value=adminloc.Adminlocation().workshifts)
           action = ActionChains(self.driver)
           action.click(on_element=workshift).perform()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().workshifts).click() 
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().workadd).click()
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().shiftinput).send_keys(info.Info().shift)  
           self.driver.find_element(by=By.XPATH, value = adminloc.Adminlocation().shiftsave).click()
           print(" job menu list are validated successfully")
           assert self.driver.current_url=='https://opensource-demo.orangehrmlive.com/web/index.php/admin/workShift'
    

       