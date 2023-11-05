from base.base_page import BasePage

class TensorAboutPage(BasePage):
    
    IMG1 = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[1]/a/div[1]/img'
    IMG2 = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[2]/a/div[1]/img'
    IMG3 = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[3]/a/div[1]/img'
    IMG4 = '//*[@id="container"]/div[1]/div/div[4]/div[2]/div[4]/a/div[1]/img'
  
    IMAGES = '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]'

    def get_size(self):
        result = False
        im1 = self.find_element(self.IMG1).rect
        #im1= {im1['height'],im1['width']}
        im2 = self.find_element(self.IMG2).rect
        im3 = self.find_element(self.IMG3).rect
        im4 = self.find_element(self.IMG4).rect
        

        if (im1['height'] == im2['height']) and (im3['height'] == im4['height']):
            if (im1['width'] == im2['width']) and (im3['width'] == im4['width']):
                result = True
                return result 
        else:
            return result


        