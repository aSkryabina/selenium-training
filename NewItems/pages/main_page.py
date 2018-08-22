class MainPage:

    def __init__(self,driver):
        self.driver = driver

    def open_page(self):
        self.driver.get("http://localhost/litecart/")
        return self

    def item_click(self):
        items = self.driver.find_elements_by_xpath("//li[contains(@class,'product')]")
        items[0].click()