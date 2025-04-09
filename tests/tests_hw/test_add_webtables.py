import time
from pages.tables import Tables

def test_add_tables(browser):
    page_tables = Tables(browser)

    page_tables.visit()
    page_tables.btn_add.click()
    time.sleep(2)
    page_tables.btn_submit.click()
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
    page_tables.correct.click()
    time.sleep(2)
    assert page_tables.modal_form.exist()
    page_tables.first_name.clear()
    assert page_tables.first_name.get_text() == ''
    page_tables.first_name.send_keys('Ivan')
    time.sleep(2)
    page_tables.btn_submit.click()
    time.sleep(2)
    assert page_tables.save_name.get_text() == 'Ivan'
    page_tables.del_new_line.click()
    time.sleep(2)
    assert not page_tables.save_name.get_text() == 'Ivan'
    assert not page_tables.save_lastname.get_text() == 'Nikitin'
    assert not page_tables.save_email.get_text() == 'info@email.com'
    assert not page_tables.save_age.get_text() == '33'
    assert not page_tables.save_salary.get_text() == '3000'
    assert not page_tables.save_department.get_text() == 'economic'
    assert not page_tables.correct.exist()
    assert not page_tables.del_new_line.exist()

