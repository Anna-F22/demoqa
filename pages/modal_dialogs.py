from components.components import WebElement
from pages.base_page import BasePage

class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btn_modal_dialog = WebElement(driver,'div:nth-child(3)>div >ul>li')
        self.btn_base_page = WebElement(driver, '#app > header > a > img')
        self.btn_small_modal = WebElement(driver, '#showSmallModal')
        self.btn_small_close = WebElement(driver, '#closeSmallModal')
        self.btn_large_modal = WebElement(driver, '#showLargeModal')
        self.btn_large_close = WebElement(driver, '#closeLargeModal')





