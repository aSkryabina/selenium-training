import pytest
from selenium import webdriver



@pytest.fixture
def driver(request):
   wd = webdriver.Chrome()
   request.addfinalizer(wd.quit)
   return wd


def test_login(driver):
    driver.get("http://google.ru/")
    driver.find_element_by_name("q").send_keys("admin")
    driver.find_element_by_name("btnK").click()

    form1 = driver.find_element_by_id("login-form")
    form2 = driver.find_element_by_tag_name("form")
    form3 = driver.find_element_by_class_name("login")
    form4 = driver.find_element_by_css_selector("form.login")
    form5 = driver.find_element_by_css_selector("#login-form")

    field1 = driver.find_element_by_name("username")
    field2 = driver.find_element_by_xpath("//input[@name='username']")
    link = driver.find_element_by_link_text("Logout")

    links = driver.find_elements_by_tag_name("a")