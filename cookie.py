import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_cookie(driver):
    driver.get("http://mailhog.app28.appdevstage.com/#")
    driver.add_cookie({'name': 'test', 'test': 'bar'})
    test_cookie = driver.get_cookie('test')
    print(test_cookie)
    cookies = driver.get_cookies()
    driver.delete_cookie('test')
    driver.delete_all_cookies()