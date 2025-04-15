from pages.modal_dialogs import ModalDialogs
import time


def test_modal_check(browser):
    modal_page = ModalDialogs(browser)
    try:
        modal_page.visit()
        assert not modal_page.alert()
        modal_page.btn_small_modal.click()
        modal_page.btn_small_close.click()
        time.sleep(2)
        assert not modal_page.alert()
        modal_page.btn_large_modal.click()
        time.sleep(2)
        modal_page.btn_large_close.click()
        assert not modal_page.alert()
    except ValueError:
        pass


