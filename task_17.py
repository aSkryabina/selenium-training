import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    wd.implicitly_wait(5)
    request.addfinalizer(wd.quit)
    return wd


def test_windows(driver):
    # авторизация в админке
    driver.get("http://localhost/litecart/admin/")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("remember_me").click()
    driver.find_element_by_name("login").click()

    driver.find_element_by_xpath("//td[@id='sidebar']//span[contains(text(),'Catalog')]").click()
    driver.find_element_by_xpath("//table[@class='dataTable']//a[contains(text(),'Rubber Ducks')]").click()
    items = driver.find_elements_by_xpath("//a[contains(.,'Duck') and not(contains(.,'Ducks'))]")
    for item in items:
        main_window = driver.current_window_handle
        old_windows = driver.window_handles
        href = item.get_attribute("href")
        driver.execute_script("window.open(\'%s\')" % href)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.new_window_is_opened(old_windows))
        new_window = [i for i in driver.window_handles if i not in old_windows]
        driver.switch_to.window(new_window[0])
        log = driver.get_log("browser")
        if log == []:
            print("Logs are empty on a page " + href)
        else:
            for l in log:
                print(l)
        driver.close()
        driver.switch_to_window(main_window)





