from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR,'#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'#add_to_basket_form > button')
    BOOK = (By.CSS_SELECTOR,'#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BOOK_IN_CART = (By.CSS_SELECTOR,'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    CART_PRICE = (By.CSS_SELECTOR,'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    CART = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    
