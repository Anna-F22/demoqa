from pages.links import Links
import time

def test_browser_tab(browser):
    page_browser = Links(browser)
    page_browser.visit()

    assert page_browser.new_window.get_text() == 'Home'
    assert page_browser.new_window.get_dom_attribute('href') == 'https://demoqa.com'

    assert len(browser.window_handles) == 1
    page_browser.new_window.click_force()
    time.sleep(2)
    assert len(browser.window_handles) == 2

