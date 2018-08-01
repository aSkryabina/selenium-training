import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def prices(driver,locator):
    list = []
    items = driver.find_elements_by_css_selector(locator)
    item = items[0]
    price_reg = item.find_element_by_css_selector("s.regular-price").text
    list.append(price_reg)
    price_sale = item.find_element_by_css_selector("strong.campaign-price").text
    list.append(price_sale)
    return list


def test_product(driver):
    driver.get("http://localhost/litecart/")
    price_main = prices(driver,"div#box-campaigns li.product")
    driver.find_element_by_css_selector("div#box-campaigns li.product").click()
    price_page = prices(driver,"div#box-product")
    if price_main == price_page:
        print("Prices are equal")



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


