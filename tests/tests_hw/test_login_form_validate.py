import time
from pages.form_page import FormPage

def test_login_validate(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute('placeholder') == 'First Name'
    assert form_page.last_name.get_dom_attribute('placeholder') == 'Last Name'
    assert form_page.user_email.get_dom_attribute('placeholder') == 'name@example.com'
    assert form_page.user_email.get_dom_attribute('pattern') == '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

    time.sleep(2)
    form_page.btn_submit.scroll_to_element()
    time.sleep(2)
    form_page.btn_submit.click_force()
    assert form_page.form_novalidate.get_dom_attribute('class') == 'was-validated'
    time.sleep(2)