import pytest
from .pages.main_page import MainPage
from .pages.product_page import BookPage
from time import sleep

url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
param_lst = [0,1,2,3,4,pytest.param('bugged_link',marks=pytest.mark.xfail),
             6,pytest.param('wrong_cart_title',marks=pytest.mark.skip),
             8,9]
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
    #sleep(180)
    assert book_title == cart_title, 'Название не сходится'
    assert book_price == cart_price, 'Цена не сходится'
    
