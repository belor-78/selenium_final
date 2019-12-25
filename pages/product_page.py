# Page Object
from .base_page import BasePage
from .locators import ProductPageLocators

class BookPage(BasePage):
    def is_promo(self):
        assert '?promo=' in self.browser.current_url, 'промо отсутствует'

    def add_to_cart(self):
        cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_btn.click()

    def book_title(self):
        book_title = self.browser.find_element(*ProductPageLocators.BOOK).text
        print(book_title)
        return book_title

    def book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        print(book_price)
        return book_price

    def book_in_cart(self):
        book_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        book_title = self.browser.find_element(*ProductPageLocators.BOOK_IN_CART).text
        print(book_title, book_price)
        return book_price, book_title

    def go_to_cart(self):
        self.browser.find_element(*ProductPageLocators.CART).click()
