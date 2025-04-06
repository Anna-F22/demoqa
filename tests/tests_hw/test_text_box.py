import time

from pages.text_box import TextBox

def test_textbox(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('tester')
    time.sleep(2)
    text_box.adr_user.send_keys('City, street, house')
    text_box.submit.click_force()
    time.sleep(2)

    assert text_box.name_sub.get_text() == 'Name:tester'
    assert text_box.adr_sub.get_text() == 'Current Address :City, street, house'

