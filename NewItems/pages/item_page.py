from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ItemPage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def items_counter_in_trash(self):
        self.driver.find_element_by_css_selector("span.quantity").text
        return int(self)

    def select_option(self):
        if self.driver.find_elements_by_xpath("select[name='options[Size]']") > 0:
            Select(self.driver.find_element_by_css_selector("select[name='options[Size]']")).select_by_visible_text(
                "Medium +$2.50")

    def add_item(self,count):
        self.driver.find_element_by_xpath("//button[@name='add_cart_product']").click()
        self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(count + 1)))
