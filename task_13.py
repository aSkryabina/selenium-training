import pytest
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import os


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

#проверка наличия элемента
def find_element(driver,locator):
    try:
        driver.find_element_by_css_selector("select[name='options[Size]']")
        return True
    except EC.NoSuchElementException:
        return False


def test_new_product(driver):
    driver.get("http://localhost/litecart/")
    # поиск всех товаров и переход в первый найденнй товар
    items = driver.find_elements_by_xpath("//li[contains(@class,'product')]")
    items[0].click()

    # если у товара есть обязательный для заполнения выпадающий список, заполняем его
    if find_element(driver,"select[name='options[Size]']"):
        Select(driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_visible_text("Medium +$2.50")
    # добавляем товар в корзину
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()

