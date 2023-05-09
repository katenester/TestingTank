# test_registration.py
import pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("name", ["Иванов Иван Иванович", "Киселева Тамара Петровна", "Lihachev Ulta", "TYTYTY HH", "д'Артаньян", "ППАА", "Hello мир", "попов нина"])
def test_registration(driver, name):
    driver.get("Tolko")
    assert "SmartFit" in driver.title
    username = driver.find_element_by_name("username")
    password = driver.find_element_by_name("password")
    submit = driver.find_element_by_name("submit")
    username.send_keys("neste")
    password.send_keys("kkkkk12")
    username.submit()
    assert "Welcome" in driver.page_source
    driver.find_element_by_link_text("Register").click()
    assert "Register" in driver.page_source
    firstname = driver.find_element_by_name("firstname")
    lastname = driver.find_element_by_name("lastname")
    email = driver.find_element_by_name("email")
    password = driver.find_element_by_name("password")
    confirmpassword = driver.find_element_by_name("confirmpassword")
    firstname.send_keys(name.split()[0])
    lastname.send_keys(name.split()[-1])
    email.send_keys("test@test.com")
    password.send_keys("password")
    confirmpassword.send_keys("password")
    submit = driver.find_element_by_name("submit")
    submit.click()
    assert "Registration successful" in driver.page_source
