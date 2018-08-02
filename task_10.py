import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import re

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def pars_color(str):
    rgb = []
    len(str)
    clr = str[5:len(str)-4]
    rgb = clr.split(", ")
    print(rgb)
    return rgb


def prices(driver,locator):
    list = []
    items = driver.find_elements_by_css_selector(locator)
    item = items[0]

    #Получаем обычную и акционную стоимость товара
    price_reg = item.find_element_by_css_selector("s.regular-price")
    price_sale = item.find_element_by_css_selector("strong.campaign-price")

    #Получаем текст
    text_pr = price_reg.text
    list.append(text_pr)
    text_ps = price_sale.text
    list.append(text_ps)

    #Получаем размер
    size_pr = price_reg.value_of_css_property("font-size")
    size_ps = price_sale.value_of_css_property("font-size")
    if size_pr < size_ps:
        print("Size of regular price less than campaign price")
    else:

        print("Size of regular price more than campaign price")
    #получаем цвет акционной цены и проверяем, является ли он серым
    color_ps_css = price_sale.value_of_css_property("color")
    color_ps = pars_color(color_ps_css)
    if color_ps[0] == color_ps[1] and color_ps[0] == color_ps[2]:
        print("The regular price's color is gray")
    else:
        print("The regular price's color is not gray")

    #получаем цвет регулярной цены
    color_pr_css = price_reg.value_of_css_property("color")
    color_pr = pars_color(color_pr_css)
    if color_pr[1] == 0 and color_pr[2] == 0:
        print("The regular price's color is red")
    else:
        print("The regular price's color is not red")

    #получаем стиль текста акционной цены
    font_ps = price_sale.value_of_css_property("text-decoration")
    #получаем стиль акционной цены
    font_pr = price_reg.value_of_css_property("font-weight")
    return list


def test_product(driver):
    #поиск элементов на главной странице
    main = []
    driver.get("http://localhost/litecart/")
    name_main = driver.find_element_by_css_selector("div#box-campaigns li.product div.name").text
    main.append(name_main)
    price_main = prices(driver,"div#box-campaigns li.product")
    main.extend(price_main)
    driver.find_element_by_css_selector("div#box-campaigns li.product").click()
    #поиск элементов на странице товара странице
    page = []
    name_page = driver.find_element_by_css_selector("h1.title").text
    page.append(name_page)
    price_page = prices(driver, "div#box-product")
    page.extend(price_page)
    #сравнение товаров
    if main == page:
        print("Are equal")
    else:
        print("Are not equal")



