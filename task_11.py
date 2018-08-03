import pytest
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd

def test_rega(driver):
    #генерация случайного имейла
    driver.get("http://localhost/litecart/")
    login = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnm') for _ in range(6))
    email = login + "@a.com"
    password = 123123

    #регистрация
    form = driver.find_element_by_css_selector("form[name=login_form]")
    form.find_element_by_css_selector("td a").click()
    driver.find_element_by_css_selector("input[name='firstname']").send_keys("Test")
    driver.find_element_by_css_selector("input[name='lastname']").send_keys("Test")
    driver.find_element_by_css_selector("input[name='address1']").send_keys("New street")
    driver.find_element_by_css_selector("input[name='postcode']").send_keys("12345")
    driver.find_element_by_css_selector("input[name='city']").send_keys("Test City")
    Select(driver.find_element_by_css_selector("select[name='country_code']")).select_by_visible_text("United States")
    Select(driver.find_element_by_css_selector("select[name='zone_code']")).select_by_visible_text("New York")
    driver.find_element_by_css_selector("input[name='email']").send_keys(email)
    driver.find_element_by_css_selector("input[name='phone']").send_keys(Keys.ENTER)
    driver.find_element_by_css_selector("input[name='phone']").send_keys(Keys.HOME + "+19211234567")
    driver.find_element_by_css_selector("input[name='password']").send_keys(password)
    driver.find_element_by_css_selector("input[name='confirmed_password']").send_keys(password)
    driver.find_element_by_css_selector("button[name='create_account']").click()

    #logout
    acc_menu = driver.find_element_by_css_selector("div#box-account")
    acc_menu.find_element_by_css_selector("li:last-child a").click()

    #авторизация
    reg_form = driver.find_element_by_css_selector("form[name=login_form]")
    reg_form.find_element_by_css_selector("input[name='email']").send_keys(email)
    reg_form.find_element_by_css_selector("input[name='password']").send_keys(password)
    reg_form.find_element_by_css_selector("button[name='login']").click()

    #logout
    acc_menu = driver.find_element_by_css_selector("div#box-account")
    acc_menu.find_element_by_css_selector("li:last-child a").click()