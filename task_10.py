import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(2)
    request.addfinalizer(wd.quit)
    return wd


def prices(driver,locator):
    list = []
    items = driver.find_elements_by_css_selector(locator)
    item = items[0]
    # Получаем обычную и акционную стоимость товара
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
    return list


def test_product(driver):
    '''поиск элементов на главной странице'''
    main = []
    driver.get("http://localhost/litecart/")
    name_main = driver.find_element_by_css_selector("div#box-campaigns li.product div.name").text
    main.append(name_main)
    price_main = prices(driver,"div#box-campaigns li.product")
    main.extend(price_main)
    driver.find_element_by_css_selector("div#box-campaigns li.product").click()
    '''поиск элементов на странице товара странице'''
    page = []
    name_page = driver.find_element_by_css_selector("h1.title").text
    page.append(name_page)
    price_page = prices(driver, "div#box-product")
    page.extend(price_page)
    '''сравнение товаров'''
    if main == page:
        print("Are equal")
    else:
        print("Are not equal")



    '''
    driver.get("http://localhost/litecart/")
    locator = "div#box-campaigns li.product"
    items = driver.find_elements_by_css_selector(locator)
    item = items[0]
    main_item = []
    name = item.find_element_by_css_selector("div.name").text
    main_item.append(name)
    price_reg = item.find_element_by_css_selector("s.regular-price").text
    main_item.append(price_reg)
    price_sale = item.find_element_by_css_selector("strong.campaign-price").text
    main_item.append(price_sale)
    price_color = item.find_element_by_css_selector("s.regular-price").value_of_css_property("color")
    price_style = item.find_element_by_css_selector("s.regular-price").value_of_css_property("text-decoration-line")
    print(price_style)
    '''


