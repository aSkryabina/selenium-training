import pytest
from selenium import webdriver
import random
from selenium.webdriver.support.ui import Select
import os


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_link(driver):
    #авторизация в админке
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_xpath("//a[@title='Edit']").click()
    form = driver.find_element_by_xpath("//form")
    links = form.find_elements_by_css_selector("a:not(#address-format-hint)")
    count = len(links)
    for i in range(count):
        links[i].click()
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
        driver.find_element_by_xpath("//a[@title='Edit']").click()
        form = driver.find_element_by_xpath("//form")
        links = form.find_elements_by_css_selector("a:not(#address-format-hint)")


