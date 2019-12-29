import pytest
from .pages.main_page import MainPage
from .pages.product_page import BookPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from time import sleep
import time
from random import choice

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
param_lst = [0,1,2,3,4,5,6,
             pytest.param('wrong_cart_title',marks=pytest.mark.skip),
             8,9]
letters = tuple('qwertyuiopasdfghjklzxcvbnm123456789QWERTYUIOPASDFGHJKLZXCVBNM')

@pytest.mark.skip
@pytest.mark.parametrize('link',param_lst)
def test_guest_can_add_product_to_basket(browser,link):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
    url = url + str(link)
    page = BookPage(browser, url)
    page.open()
    page.is_promo()
    book_title = page.book_title()
    book_price = page.book_price()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    sleep(2)
    cart_price, cart_title = page.book_in_cart()
    assert book_title == cart_title, 'Название не сходится'
    assert book_price == cart_price, 'Цена не сходится'

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = BookPage(browser,url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = BookPage(browser,url)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = BookPage(browser,url)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.element_should_be_gone()

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = MainPage(browser, link)
    page.open()
    page.should_by_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BookPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = BasketPage(browser,url)
    page.open()
    page.go_to_cart()
    page.empty_basket()
    page.empty_basket_text()


@pytest.mark.need_review
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, url)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + '@ksdjfbv.org'
        password = ''.join([choice(letters) for i in range(10)])
        page.register_new_user(email, password)
        page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        page = BookPage(browser, browser.current_url)
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        #url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = BookPage(browser, url)
        page.open()
        book_title = page.book_title()
        book_price = page.book_price()
        page.add_to_cart()
        sleep(2)
        cart_price, cart_title = page.book_in_cart()
        assert book_title == cart_title, 'Название не сходится'
        assert book_price == cart_price, 'Цена не сходится'
