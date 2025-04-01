import time

from pages.accordion import Accordion

def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.section_cont.visible()
    accordion_page.section_head.click()
    time.sleep(2)
    assert not accordion_page.section_cont.visible()

def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.section_two.visible()
    assert not accordion_page.section_two_one.visible()
    assert not accordion_page.section_three.visible()


