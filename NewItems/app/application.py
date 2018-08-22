from selenium import webdriver
from NewItems.pages.main_page import MainPage
from NewItems.pages.item_page import ItemPage
from NewItems.pages.trash_page import TrashPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.item_page = ItemPage(self.driver)
        self.trash_page = TrashPage(self.driver)

    def quit(self):
        self.driver.quit()

    def add_items(self):
        self.main_page.open_page()
        self.main_page.item_click()
        count = int(self.item_page.get_items_counter_in_trash())
        self.item_page.select_option()
        self.item_page.add_item(count)

    def get_trash_count(self):
        self.trash_page.open_page()
        count = len(self.trash_page.get_items_in_trash())
        return count

    def delete_items(self,count):
        list = self.trash_page.get_items_in_trash()
        el = list[count-1]
        self.trash_page.select_item()
        self.trash_page.delete_item(el)