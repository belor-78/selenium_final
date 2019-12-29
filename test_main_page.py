import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        self.page = MainPage(browser,link)
        self.page.open()
        self.page.should_by_login_link()

    #@pytest.mark.skip
    def test_guest_can_go_to_login_page(self, browser):
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

@pytest.mark.skip
def test_should_be_login_page(browser):
    url = browser.current_url
    print(url)
    page = LoginPage(browser, url)
    page.should_be_login_page()

@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser,link)
    page.open()
    page.go_to_cart()
    page.empty_basket()
    page.empty_basket_text()

    
