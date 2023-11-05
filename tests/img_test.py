from page.sbis_page import SbisPage 
from page.sbis_contact_page import SbisContactPage 
from page.tensor_page import TensorPage
from page.sbis_page import SbisPage 
from page.tensor_about_page import TensorAboutPage
from config.links import Links


class TestProfile():

    '''
    def test_img(self,driver):
       sbis = SbisPage(driver,Links.SBIS_URL)
       tensor = TensorPage(driver,Links.TENSOR_URL)
       sbis_con = SbisContactPage(driver,Links.SBIS_CONT_URL)
       tensor_about = TensorAboutPage(driver,Links.TENSOR_ABOUT_URL)
       sbis.open()
       #assert Links.SBIS_URL == sbis.current_url(), "Ошибка по URL" 
       sbis.contact_link()
       sbis_con.open()
       sbis_con.tensor_link()
       tensor.open()
       tensor.go_to_strength_in_people()
       tensor_about.open()
       assert Links.TENSOR_ABOUT_URL == sbis.current_url(), "Ошибка по URL" 
       assert tensor_about.get_size() == True
    
    def test_location(self,driver):
        sbis = SbisPage(driver,Links.SBIS_URL)
        sbis_con = SbisContactPage(driver,Links.SBIS_CONT_URL)
        sbis.open()
        sbis.contact_link()
        assert sbis_con.checking_the_region() == "Тюменская обл.", "Wrong region"
        assert sbis_con.checking_the_list_of_partners() == "Тюмень"
        assert len(sbis_con.check_partners()) >=1 , "No partners found!"
        sbis_con.open_change_region()
        sbis_con.change_region_to_kamchatka()
        assert sbis_con.current_url() == Links.KAMCHATKA_REGION_URL, "Wrong region link"
        assert sbis_con.current_title() == "СБИС Контакты — Камчатский край" , "Wrong region title"
        assert sbis_con.checking_the_region() == "Камчатский край", "Wrong region"
        assert sbis_con.checking_the_list_of_partners() == "Петропавловск-Камчатский"
        assert len(sbis_con.check_partners()) >=1 , "No partners found!"

    '''

    
    def test_download(self,driver):
        sbis = SbisPage(driver,Links.SBIS_URL)
        sbis.open()
        sbis.download_link()


