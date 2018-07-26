import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd

def test_stickers(driver):
    driver.get("http://localhost/litecart/")
    ducks = driver.find_elements_by_xpath("//div[contains(@class,'image-wrapper')]")
    for duck in ducks:
        stickers = duck.find_elements_by_xpath(".//div[contains(@class,'sticker')]")
        len(stickers) == 1



