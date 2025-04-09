import time
from pages.tables import Tables

def test_tables_page(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    page_tables.btn_select_rows.scroll_to_element()
    page_tables.btn_select_rows.click()
    time.sleep(3)

    assert page_tables.btn_next.get_dom_attribute('disabled')
    assert page_tables.btn_prev.get_dom_attribute('disabled')

    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.modal_form.exist()

    page_tables.first_name.send_keys('Nik')
    page_tables.last_name.send_keys('Nikitin')
    time.sleep(2)
    page_tables.email.send_keys('info@email.com')
    page_tables.age.send_keys('33')
    time.sleep(2)
    page_tables.salary.send_keys('3000')
    page_tables.department.send_keys('economic')
    time.sleep(2)
    page_tables.btn_submit.click()
    assert not page_tables.modal_form.exist()
    assert page_tables.save_name.get_text() == 'Nik'
    assert page_tables.save_lastname.get_text() == 'Nikitin'
    assert page_tables.save_email.get_text() == 'info@email.com'
    assert page_tables.save_age.get_text() == '33'
    assert page_tables.save_salary.get_text() == '3000'
    assert page_tables.save_department.get_text() == 'economic'


    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.modal_form.exist()

    page_tables.first_name.send_keys('Ivan')
    page_tables.last_name.send_keys('Sergeev')
    time.sleep(2)
    page_tables.email.send_keys('sale@mail.ry')
    page_tables.age.send_keys('37')
    time.sleep(2)
    page_tables.salary.send_keys('4000')
    page_tables.department.send_keys('informtech')
    time.sleep(2)
    page_tables.btn_submit.click()
    assert not page_tables.modal_form.exist()
    assert page_tables.five_name.get_text() == 'Ivan'
    assert page_tables.five_lastname.get_text() == 'Sergeev'
    assert page_tables.five_email.get_text() == 'sale@mail.ry'
    assert page_tables.five_age.get_text() == '37'
    assert page_tables.five_salary.get_text() == '4000'
    assert page_tables.five_depart.get_text() == 'informtech'
    time.sleep(2)

    page_tables.btn_add.click()
    time.sleep(2)
    assert page_tables.modal_form.exist()

    page_tables.first_name.send_keys('Roman')
    page_tables.last_name.send_keys('Sobolev')
    time.sleep(2)
    page_tables.email.send_keys('test@test.com')
    page_tables.age.send_keys('35')
    time.sleep(2)
    page_tables.salary.send_keys('5000')
    page_tables.department.send_keys('logistic')
    time.sleep(2)
    page_tables.btn_submit.click()
    page_tables.btn_next.click()

    assert not page_tables.modal_form.exist()
    assert page_tables.nextpage_name.get_text() == 'Roman'
    assert page_tables.nextpage_lastname.get_text() == 'Sobolev'
    assert page_tables.nextpage_email.get_text() == 'test@test.com'
    assert page_tables.nextpage_age.get_text() == '35'
    assert page_tables.nextpage_salary.get_text() == '5000'
    assert page_tables.nextpage_depart.get_text() == 'logistic'
    time.sleep(2)

    page_tables.btn_prev.click()
    time.sleep(2)




