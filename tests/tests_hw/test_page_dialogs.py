from pages.modal_dialogs import ModalDialogs
from pages.demoqa import DemoQa

def test_modal_elements(browser):
    modal_page = ModalDialogs(browser)
    modal_page.visit()

    assert modal_page.btn_modal_dialog.check_count_elements(count=5)

def test_navigation_modal(browser):
    demo_qa_page = DemoQa(browser)
    modal_page = ModalDialogs(browser)

    modal_page.visit()
    browser.refresh()
    modal_page.btn_base_page.click()
    browser.back()
    browser.set_window_size(1000, 300)
    browser.forward()
    assert demo_qa_page.equal_url()
    assert browser.title == 'DEMOQA'
    browser.set_window_size(1000, 1000)





