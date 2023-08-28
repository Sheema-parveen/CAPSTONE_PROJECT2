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

    def test_admin_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           adminmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().admin)))
           adminmodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'
        
    def test_pim_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           pimmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().pim)))
           pimmodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList'

    def test_leave_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           leavemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().leave)))
           leavemodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList'
        
    def test_time_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           timemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().time)))
           timemodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'
    
    def test_recruitment_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           recruit_module = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().recruitment)))
           recruit_module.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'
    
    def test_myinfo_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           myinfomodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().myinfo)))
           myinfomodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7'
        
    def test_performance_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           performancemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().performance)))
           performancemodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview'
    
    def test_dashboard_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           dashboardmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().dashboard)))
           dashboardmodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
    
    def test_directory_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           directorymodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().directory)))
           directorymodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory'
        
    def test_maintenance_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           maintenancemodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().maintenance)))
           maintenancemodule.click()
           assert self.driver.current_url =='https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee'
    
    def test_claim_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           claimmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().claim)))
           claimmodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/claim/viewAssignClaim'

    def test_buzz_module(self,startup):
         
        if(self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"):
           self.driver.find_element(by=By.XPATH,value=location.Location().admin).click()
            
           buzzmodule = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, location.Location().buzz)))
           buzzmodule.click()
           assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz'
