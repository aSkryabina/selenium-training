from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TrashPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self):
        self.driver.find_element_by_xpath("//a[contains(text(),'Checkout »')]").click()

    def get_items_in_trash(self):
        self.driver.find_elements_by_css_selector("td.item")
        return self

    def select_item(self):
        if self.driver.find_elements_by_css_selector("li.shortcut a") > 0:
            self.driver.find_element_by_css_selector("li.shortcut a").click()

    def delete_item(self,el):
        self.driver.find_element_by_xpath("//button[@name='remove_cart_item']").click()
        self.wait.until(EC.staleness_of(el))