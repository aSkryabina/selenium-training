import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(1)
    request.addfinalizer(wd.quit)
    return wd


def test_countries(driver):
    '''авторизация в админке'''
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    '''проверка сортировки в разделе "Countries"'''
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    #поиск всех строк таблицы Countries, создание пустого списка и вычисление количества строк
    rows = driver.find_elements_by_css_selector("table.dataTable tr.row")
    countries = []
    count = len(rows)
    #прохождение по циклу с распарсиванием строки, записью стран в новый список и проверкой количества зон
    for i in range(count):
        row = rows[i]
        country = row.find_element_by_xpath("./td[5]").text
        zone_counter = int(row.find_element_by_xpath("./td[6]").text)
        #если зон больше 0, то переходим в карточку страны
        if zone_counter > 0:
            row.find_element_by_xpath("./td[5]/a").click()
            lines = driver.find_elements_by_css_selector("table#table-zones tr")
            counter = len(lines)
            zones = []
            # прохождение по циклу (исключая первый и последний элемент) с распарсиванием строки и записью зон в новый список
            for j in range(1,counter-1):
                line = lines[j]
                zone = line.find_element_by_xpath("./td[3]").text
                zones.append(zone)
            # сравнение исходного списка зон с отсортированным списком
            table = driver.find_element_by_css_selector("table")
            zones_url = table.get_attribute("baseURI")
            if sorted(zones) == zones:
                print('The list of zones on page ' + zones_url + ' is sorted')
            else:
                print('The list of zones on page ' + zones_url + ' is not sorted')
            #возвращение на страницу Countries и новый поиск всех строк таблицы
            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
            rows = driver.find_elements_by_css_selector("table.dataTable tr.row")
        countries.append(country) #добавление страны в список
    #сравнение исходного списка стран с отсортированным списком
    table = driver.find_element_by_css_selector("table")
    countries_url = table.get_attribute("baseURI")
    if sorted(countries) == countries:
        print('The list of countries on page ' + countries_url + ' is sorted')
    else:
        print('The list of countries on page ' + countries_url + ' is not sorted')


    '''проверка сортировки в разделе "Geo Zones"'''
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    # поиск всех строк таблицы Geo Zones, создание пустого списка и вычисление количества строк
    rows = driver.find_elements_by_css_selector("table.dataTable tr.row")
    count = len(rows)
    # прохождение по циклу с распарсиванием строки, записью стран в новый список и проверкой количества зон
    for i in range(count):
        row = rows[i]
        row.find_element_by_xpath("./td[3]/a").click()
        lines = driver.find_elements_by_css_selector("table#table-zones tr")
        counter = len(lines)
        zones = []
        # прохождение по циклу (исключая первый и последний элемент) с распарсиванием строки и записью выбранных в выпадающем списке зон в новый список
        for j in range(1, counter - 1):
            line = lines[j]
            zone = line.find_element_by_xpath("./td[3]//option[@selected]").text
            zones.append(zone)
        # сравнение исходного списка зон с отсортированным списком
        table = driver.find_element_by_css_selector("table")
        zones_url = table.get_attribute("baseURI")
        if sorted(zones) == zones:
            print('The list of zones on page ' + zones_url + ' is sorted')
        else:
            print('The list of zones on page ' + zones_url + ' is not sorted')
        #возвращение на страницу Geo Zones и новый поиск всех строк таблицы
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
        rows = driver.find_elements_by_css_selector("table.dataTable tr.row")