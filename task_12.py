import pytest
from selenium import webdriver
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(1)
    request.addfinalizer(wd.quit)
    return wd


def test_countries(driver):
    #авторизация в админке
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    #переход в каталог товаров и добавление всех товаров в список
    menu = driver.find_elements_by_xpath("//ul[@id='box-apps-menu']//li[@id='app-']")
    menu[1].click()
    table = driver.find_element_by_css_selector(".dataTable")
    rows = table.find_elements_by_xpath("//tr[contains(@class,'row')]")
    start_list = len(rows)

    #переход в карточку добавления товара
    buttons = driver.find_elements_by_css_selector("a.button")
    buttons[1].click()

    #генерация данных
    name = "item" + str(random.randint(1,999))
    code = str(random.randint(1,999))
    keywords = "toys"
    short_description = "The best"
    description = "The best of the best"
    head_title = "Dool"
    meta_description = "girls"

    #вкладка "General"
    driver.find_element_by_css_selector("input[type=radio][value='1']").click()
    driver.find_element_by_css_selector("input[name='name[en]']").send_keys(name)
    driver.find_element_by_css_selector("input[name='code']").send_keys(code)
    driver.find_element_by_css_selector("input[type='checkbox'][name='product_groups[]'][value='1-2']").click()
    driver.find_element_by_css_selector("input[type='number'][name='quantity']").click()
    driver.find_element_by_css_selector("input[type='number'][name='quantity']").clear()
    driver.find_element_by_css_selector("input[type='number'][name='quantity']").send_keys("19,99")

    #загрузка изображения
    path = os.path.join(os.path.dirname(__file__))
    driver.find_element_by_css_selector("input[type='file'][name='new_images[]']").send_keys(path + "\\123.jpg")

    #календарь
    driver.execute_script("$('%s').datepicker('setDate', '%s')" % (driver.find_element_by_css_selector("input[type='date'][name='date_valid_from']"), "02/20/2002"))
    #driver.execute_script("$('%s').datepicker('setDate', '%s')" % (driver.find_element_by_css_selector("input[type='date'][name='date_valid_to']"), "02/20/2002"))

    #вкладка "Information"
    driver.find_element_by_xpath("//a[contains(text(),'Information')]").click()
    Select(driver.find_element_by_css_selector("select[name='manufacturer_id']")).select_by_visible_text("ACME Corp.")
    driver.find_element_by_css_selector("input[name='keywords']").send_keys(keywords)
    driver.find_element_by_css_selector("input[name='short_description[en]']").send_keys(short_description)
    driver.find_element_by_css_selector("div.trumbowyg-editor").send_keys(description)
    driver.find_element_by_css_selector("input[name='head_title[en]']").send_keys(head_title)
    driver.find_element_by_css_selector("input[name='meta_description[en]']").send_keys(meta_description)

    #вкладка "Prices"
    driver.find_element_by_xpath("//a[contains(text(),'Prices')]").click()
    driver.find_element_by_css_selector("input[type='number'][name='purchase_price']").click()
    driver.find_element_by_css_selector("input[type='number'][name='purchase_price']").clear()
    driver.find_element_by_css_selector("input[type='number'][name='purchase_price']").send_keys("19,99")
    Select(driver.find_element_by_css_selector("select[name='purchase_price_currency_code']")).select_by_visible_text("US Dollars")
    driver.find_element_by_css_selector("input[type='text'][name='prices[USD]']").send_keys("19,99")
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[USD]']").click()
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[USD]']").clear()
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[USD]']").send_keys("1,99")
    driver.find_element_by_css_selector("input[type='text'][name='prices[EUR]']").send_keys("15,99")
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[EUR]']").click()
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[EUR]']").clear()
    driver.find_element_by_css_selector("input[type='number'][name='gross_prices[EUR]']").send_keys("0,99")

    #сохранение
    driver.find_element_by_css_selector("button[type='submit'][name='save']").click()

    #проверка на отображение созданного товара в каталоге
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog")
    table = driver.find_element_by_css_selector(".dataTable")
    rows = table.find_elements_by_xpath("//tr[contains(@class,'row')]")
    if len(rows) == start_list+1:
        print("Changes were successfully saved.")
    else:
        print("Error")


