import os
from base.base_page import BasePage


class DownloadPage(BasePage):
    SBIS_PLUGIN = "//div[text()='СБИС Плагин']"
    PUGIN_DOWNLOAD_LINK = "//a[@href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']"

    def switch_the_download_menu(self):
        pass

    def download_file(self):
        self.find_element(self.PUGIN_LINK).click()

    def get_size_info(self):
        self.find_element(self.PUGIN_DOWNLOAD_LINK).text    
    
    def file_size_comparisons(self):
        pass
    