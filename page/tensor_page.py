import time
from base.base_page import BasePage


class TensorPage(BasePage):
    STRENGTH_IN_PEOPLE = ("xpath","//*[@id='container']/div[2]/div[2]")
    STRENGTH = ("//*[@id='container']/div[1]/div/div[5]/div/div")
    TENSOR_ABOUT_LINK = ("xpath","(//a[@href='/about'])[2]")

    def go_to_strength_in_people(self):
        time.sleep(4)
        
        self.go_to_element(self.STRENGTH)
        self.element_is_visible(self.TENSOR_ABOUT_LINK).click()
    
    
        
        