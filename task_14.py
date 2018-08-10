import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.support.ui import Select
import os


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_windows(driver):

    def there_is_window_other_than(old_windows):
        new_windows = driver.window_handles
        count = len(old_windows)
        for i in range(count):
            new_windows.remove(old_windows[i])
        new = new_windows[0]
        return new

    # авторизация в админке
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    # страница countries
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    # поиск внешних ссылок
    driver.find_element_by_xpath("//a[@title='Edit']").click()
    form = driver.find_element_by_xpath("//form")
    links = form.find_elements_by_css_selector("a:not(#address-format-hint)")
    count = len(links)
    # переход по каждой ссылке из списка
    for i in range(count):
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        links[i].click()
        wait = WebDriverWait(driver, 10)
        new_window = wait.until(there_is_window_other_than(old_windows))
        driver.switch_to.window(new_window)
        driver.close()
        driver.switch_to_window(main_window)


