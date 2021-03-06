from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')


class LoginPageLocators():
    REGISTRATION_FORM = (By.CSS_SELECTOR,'#register_form')
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR,'#id_registration-password1')
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER = (By.CSS_SELECTOR,'[name="registration_submit"]')


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR,'#add_to_basket_form > button')
    BOOK = (By.CSS_SELECTOR,'#content_inner > article > div.row > div.col-sm-6.product_main > h1')
    BOOK_IN_CART = (By.CSS_SELECTOR,'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    CART_PRICE = (By.CSS_SELECTOR,'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)')
    BOOK_PRICE = (By.CSS_SELECTOR, '#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color')
    CART = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicoin.alert-success')


class BasketPageLocators():
    BASKET_ITEM = (By.ID, 'basket_formset')
    BASKET = (By.ID, 'content_inner')



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR,'#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR,'#login_link_inc')
    CART = (By.CSS_SELECTOR, '#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
