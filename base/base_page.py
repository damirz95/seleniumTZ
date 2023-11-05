from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class BasePage():

    def __init__(self,driver,url):
        self.driver = driver
        self.url = url
        

    def open(self):
        self.driver.get(self.url)
        
    def current_url(self):
        return (self.driver.current_url)
    
    def current_title(self):
        return (self.driver.title)
    
    def find_element(self,locator):
        element = self.driver.find_element(By.XPATH,locator)
        return element
    
    def find_elements(self,locator):
        elements = self.driver.find_elements(By.XPATH,locator)
        return elements
    
    def element_is_visible(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.visibility_of_element_located(locator))
    
    def elements_are_visible(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.visibility_of_all_elements_located(locator))
    
    def element_is_present(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.presence_of_element_located(locator))
    
    def element_are_present(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.presence_of_all_elements_located(locator))
    
    def element_is_not_visible(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.invisibility_of_element(locator))
    
    def element_is_clickable(self,locator,timeout=10):
        #el = self.driver.find_element(By.XPATH,locator)
        return wait(self.driver,timeout).until(EC.element_to_be_clickable(locator))
    
    def go_to_element(self,element):
        el = self.driver.find_element(By.XPATH,element)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)


