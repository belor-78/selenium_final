# Page Object
from .base_page import BasePage
from .locators import ProductPageLocators

class BookPage(BasePage):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.price = None
        self.title = None
        self.cart_price, self.cart_title = None, None
    def is_promo(self):
        assert '?promo=' in self.browser.current_url, 'промо отсутствует'

    def add_to_cart(self):
        cart_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        cart_btn.click()

    def book_title(self):
        self.book_title = self.browser.find_element(*ProductPageLocators.BOOK).text
        
    def book_price(self):
        self.book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        
    def book_in_cart(self):
        self.book_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        self.book_title = self.browser.find_element(*ProductPageLocators.BOOK_IN_CART).text

    def valid_items(self):
        assert self.title == self.cart_title, 'Название не сходится'
        assert self.price == self.cart_price, 'Цена не сходится'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Success message is preswnted, but shoud not be'

    def element_should_be_gone(self):
        assert self.is_disapeared(*ProductPageLocators.SUCCESS_MESSAGE),\
               'Message still hear'


            

    
