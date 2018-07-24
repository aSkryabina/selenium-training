import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    #wd.implicitly_wait(10)
    #element = wd.find_element_by_name("q")
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()
    driver.find_element_by_id("box-apps-menu")
    driver.find_element_by_link_text("Appearence").click()
    driver.find_element_by_link_text("Template").click()
    driver.find_element_by_link_text("Logotype").click()
    driver.find_element_by_link_text("Catalog").click()
    driver.find_element_by_xpath("//li[@id='doc-catalog']//span[.='Catalog']").click()
    driver.find_element_by_link_text("Product Groups").click()
    driver.find_element_by_link_text("Option Groups").click()
    driver.find_element_by_link_text("Manufacturers").click()
    driver.find_element_by_link_text("Suppliers").click()
    driver.find_element_by_link_text("Delivery Statuses").click()
    driver.find_element_by_link_text("Sold Out Statuses").click()
    driver.find_element_by_link_text("Quantity Units").click()
    driver.find_element_by_link_text("CSV Import/Export").click()
    driver.find_element_by_link_text("Countries").click()
    driver.find_element_by_link_text("Currencies").click()
    driver.find_element_by_link_text("Customers").click()
    driver.find_element_by_xpath("//li[@id='doc-customers']//span[.='Customers']").click()
    driver.find_element_by_link_text("CSV Import/Export").click()
    driver.find_element_by_link_text("Newsletter").click()
    driver.find_element_by_link_text("Geo Zones").click()
    driver.find_element_by_link_text("Languages").click()
    driver.find_element_by_xpath("//li[@id='doc-languages']//span[.='Languages']").click()
    driver.find_element_by_link_text("Storage Encoding").click()
    driver.find_element_by_link_text("Modules").click()
    driver.find_element_by_link_text("Background Jobs").click()
    driver.find_element_by_link_text("Customer").click()
    driver.find_element_by_link_text("Shipping").click()
    driver.find_element_by_link_text("Payment").click()
    driver.find_element_by_link_text("Order Total").click()
    driver.find_element_by_link_text("Order Success").click()
    driver.find_element_by_link_text("Order Action").click()
    driver.find_element_by_link_text("Orders").click()
    driver.find_element_by_xpath("//li[@id='doc-orders']//span[.='Orders']").click()
    driver.find_element_by_link_text("Order Statuses").click()
    driver.find_element_by_link_text("Pages").click()
    driver.find_element_by_link_text("Reports").click()
    driver.find_element_by_link_text("Monthly Sales").click()
    driver.find_element_by_link_text("Most Sold Products").click()
    driver.find_element_by_link_text("Most Shopping Customers").click()
    driver.find_element_by_link_text("Settings").click()
    driver.find_element_by_link_text("Store Info").click()
    driver.find_element_by_link_text("Defaults").click()
    driver.find_element_by_link_text("General").click()
    driver.find_element_by_link_text("Listings").click()
    driver.find_element_by_link_text("Images").click()
    driver.find_element_by_link_text("Checkout").click()
    driver.find_element_by_link_text("Advanced").click()
    driver.find_element_by_link_text("Security").click()
    driver.find_element_by_link_text("Slides").click()
    driver.find_element_by_link_text("Tax").click()
    driver.find_element_by_link_text("Tax Classes").click()
    driver.find_element_by_link_text("Tax Rates").click()
    driver.find_element_by_link_text("Translations").click()
    driver.find_element_by_link_text("Search Translations").click()
    driver.find_element_by_link_text("Scan Files").click()
    driver.find_element_by_link_text("CSV Import/Export").click()
    driver.find_element_by_link_text("Users").click()
    driver.find_element_by_link_text("vQmods").click()






    #WebDriverWait(driver, 10).until(EC.title_is("My Store"))