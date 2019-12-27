from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoSuchElementException

class BasketPage(BasePage):
    def empty_basket_text(self):
        assert '\n' not in self.browser.find_element(*BasketPageLocators.BASKET).text,\
               'Большой текст'

    def basket_is_empty(self):
        try:
            self.browser.find_element(*BasketPageLocators.BASKET_ITEM)
        except NoSuchElementException:
            return True
        return False

    def empty_basket(self):
        assert self.basket_is_empty(), 'Корзина не пуста'
