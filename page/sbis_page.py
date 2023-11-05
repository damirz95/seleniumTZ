from base.base_page import BasePage



class SbisPage(BasePage):
    SBIS_CONTACT_LINK = ("xpath","(//a[@href='/contacts'])[1]")
    DOWNLOAD_LINK = ("//a[text()='Скачать СБИС']")

    def contact_link(self):
        
        self.element_is_visible(self.SBIS_CONTACT_LINK).click()

    def download_link(self):
        
        self.go_to_element(self.DOWNLOAD_LINK)
        self.find_element(self.DOWNLOAD_LINK).click()