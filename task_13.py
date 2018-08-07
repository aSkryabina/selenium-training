import pytest
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
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
        driver.find_element_by_css_selector(locator)
        return True
    except EC.NoSuchElementException:
        return False

# добавление товара в корзину
def add_item(driver):
    driver.get("http://localhost/litecart/")
    # проверяем текущее количество товаров в корзине
    count = int(driver.find_element_by_css_selector("span.quantity").text)
    # поиск всех товаров и переход в первый найденнй товар
    items = driver.find_elements_by_xpath("//li[contains(@class,'product')]")
    items[0].click()
    # если у товара есть обязательный для заполнения выпадающий список, заполняем его
    if find_element(driver, "select[name='options[Size]']"):
        Select(driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_visible_text(
            "Medium +$2.50")
    # добавляем товар в корзину
    driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
    return count


# удаление товара из корзины
def delete_item(driver):
    # переходим в корзину
    driver.get("http://localhost/litecart/en/checkout")
    # находим количество товаров в таблице
    rows = driver.find_elements_by_css_selector("td.item")
    count = len(rows)
    row = rows[count-1]
    # если товаров больше одного, то выбираем один из товаров
    if find_element(driver,"li.shortcut a"):
        driver.find_element_by_css_selector("li.shortcut a").click()
    # удаляем товар
    driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()
    # дожидаемся обновления таблицы
    wait = WebDriverWait(driver, 10)
    wait.until(EC.staleness_of(row))


def test_trash(driver):
    items_count = 3
    for i in range(items_count):
        count = add_item(driver) + 1
        wait = WebDriverWait(driver, 10)
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"span.quantity"), str(count)))
    for i in range(items_count):
        delete_item(driver)



