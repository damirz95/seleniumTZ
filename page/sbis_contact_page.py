import time
from base.base_page import BasePage


class SbisContactPage(BasePage):
    TENSOR_LINK = ("xpath","(//a[@href='https://tensor.ru/'])[1]")
    REGION = ("xpath","(//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    REGION_NON_XPATH = ("//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    KAMCHATKA_REGION = ("xpath","//*[@id='popup']/div[2]/div/div[2]/div/ul/li[43]/span")
    PARTNERS = ("//div[@id='city-id-2']")
    PARTNERS_LIST = "//div[@item-parent-key='-2']"

    def tensor_link(self):
        time.sleep(2)
        self.element_is_visible(self.TENSOR_LINK).click()
        
    
    def checking_the_region(self):
        return self.find_element(self.REGION_NON_XPATH).text
        
    def checking_the_list_of_partners(self):
        return self.find_element(self.PARTNERS).text
    def check_partners(self):
        return self.find_elements(self.PARTNERS_LIST)
    
    def open_change_region(self):
        self.find_element(self.REGION_NON_XPATH).click()

    def change_region_to_kamchatka(self):
        self.element_is_clickable(self.KAMCHATKA_REGION).click()
        time.sleep(3)
    