import time
from pages.tables import Tables

def test_sort_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    assert page_tables.str_alden_two.get_dom_attribute('class') == 'rt-tr -even'

    page_tables.sort_first.click_force()
    assert page_tables.str_alden_f.get_dom_attribute('class') == 'rt-tr -odd'

    assert page_tables.str_cierra_two.get_dom_attribute('class') == 'rt-tr -even'
    page_tables.sort_last.click_force()
    assert page_tables.str_cierra_three.get_dom_attribute('class') == 'rt-tr -odd'

    page_tables.sort_age.click_force()
    assert page_tables.str_cierra_two.get_dom_attribute('class') == 'rt-tr -even'
    time.sleep(3)

    page_tables.sort_last.click_force()
    assert page_tables.str_cierra_three.get_dom_attribute('class') == 'rt-tr -odd'
    page_tables.sort_email.click_force()
    assert page_tables.str_cierra_two.get_dom_attribute('class') == 'rt-tr -even'

    page_tables.sort_last.click_force()
    assert page_tables.str_cierra_three.get_dom_attribute('class') == 'rt-tr -odd'
    page_tables.sort_salary.click_force()
    assert page_tables.str_cierra_two.get_dom_attribute('class') == 'rt-tr -even'

    page_tables.sort_last.click_force()
    assert page_tables.str_cierra_three.get_dom_attribute('class') == 'rt-tr -odd'
    page_tables.sort_salary.click_force()
    assert page_tables.str_cierra_two.get_dom_attribute('class') == 'rt-tr -even'








