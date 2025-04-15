from pages.base_page import BasePage
from components.components import WebElement

class Tables(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)

        self.no_data = WebElement(driver, 'div.rt-noData')
        self.btn_delete_row = WebElement(driver, 'span:nth-child(2)>svg')

        self.btn_add = WebElement(driver, '#addNewRecordButton')
        self.btn_submit = WebElement(driver, '#submit')
        self.modal_form = WebElement(driver, 'body > div.fade.modal.show > div > div')

        self.first_name = WebElement(driver, '#firstName')
        self.last_name = WebElement(driver, '#lastName')
        self.email = WebElement(driver, '#userEmail')
        self.age = WebElement(driver, '#age')
        self.salary = WebElement(driver, '#salary')
        self.department = WebElement(driver, '#department')

        self.correct = WebElement(driver, '#edit-record-4 > svg > path')

        self.save_name = WebElement(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.save_lastname = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(2)')
        self.save_email = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(4)')
        self.save_age = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(3)')
        self.save_salary = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(5)')
        self.save_department = WebElement(driver, 'div:nth-child(4) > div > div:nth-child(6)')

        self.five_name = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(1)')
        self.five_lastname = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(2)')
        self.five_email = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(4)')
        self.five_age = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(3)')
        self.five_salary = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(5)')
        self.five_depart = WebElement(driver, 'div:nth-child(5) > div > div:nth-child(6)')

        self.del_new_line = WebElement(driver, '#delete-record-4 > svg > path')

        self.btn_next = WebElement(driver, 'div.-next > button')
        self.btn_prev = WebElement(driver, 'div.-previous > button')
        self.btn_select_rows = WebElement(driver, "//*[contains(text(), '5 rows')]", 'xpath')

        self.nextpage_name = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(1)')
        self.nextpage_lastname = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(2)')
        self.nextpage_email = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(4)')
        self.nextpage_age = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(3)')
        self.nextpage_salary = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(5)')
        self.nextpage_depart = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div > div:nth-child(6)')

        self.sort_first = WebElement(driver, 'div:nth-child(1) > div.rt-resizable-header-content')
        self.sort_last = WebElement(driver, 'div:nth-child(2) > div.rt-resizable-header-content')
        self.sort_age = WebElement(driver, 'div:nth-child(3) > div.rt-resizable-header-content')
        self.sort_email = WebElement(driver, 'div:nth-child(4) > div.rt-resizable-header-content')
        self.sort_salary = WebElement(driver, 'div:nth-child(5) > div.rt-resizable-header-content')
        self.sort_depart = WebElement(driver, 'div:nth-child(6) > div.rt-resizable-header-content')

        self.str_alden_two = WebElement(driver, 'div.rt-tbody > div:nth-child(2) > div')
        self.str_alden_f = WebElement(driver, 'div.rt-tbody > div:nth-child(1) > div')
        self.str_alden_three = WebElement(driver, 'div.rt-tbody > div:nth-child(3) > div')

        self.str_cierra_two = WebElement(driver, 'div.rt-tbody > div:nth-child(2) > div')
        self.str_cierra_three = WebElement(driver, 'div.rt-tbody > div:nth-child(3) > div')







