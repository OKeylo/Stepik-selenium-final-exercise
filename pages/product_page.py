from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not presented"
    
    def check_book_name(self):
        book_name_text = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        book_name_msg_text = self.browser.find_element(*ProductPageLocators.BOOK_NAME_MSG).text
        print(book_name_text + " == " + book_name_msg_text)
        assert book_name_text == book_name_msg_text, "didnt match books name"

    def check_book_price(self):
        book_price_text = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        book_price_msg_text = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_MSG).text
        print(book_price_text + " == " + book_price_msg_text)
        assert book_price_text == book_price_msg_text, "didnt match books price"

    def click_on_add_to_basket_button(self):
        button_el = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_el.click()