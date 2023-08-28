from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from Test_Information import info
from Test_Location import location
import pytest

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
   
    # reset password
    def test_forgot(self, startup):
        self.driver.get(info.Info().url)
        self.driver.implicitly_wait(10)
        self.driver.find_element(by=By.XPATH,value=location.Location().forgot_password).click()
        self.driver.find_element(by=By.NAME,value=location.Location().Username_inputbox).send_keys(info.Info().Username)
        self.driver.find_element(by=By.XPATH, value=location.Location().reset_button).click()
        assert self.driver.current_url == 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset'
        print("Reset password link sent successfully")
