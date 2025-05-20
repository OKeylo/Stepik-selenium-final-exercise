from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert login_url.find("login") >= 0, "substring 'login' is not present in current browser URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_field.send_keys(email)
        
        password1_field = self.browser.find_element(*LoginPageLocators.PASSWORD1_INPUT)
        password1_field.send_keys(password)
        
        password2_field = self.browser.find_element(*LoginPageLocators.PASSWORD2_INPUT)
        password2_field.send_keys(password)

        register_submit_button = self.browser.find_element(*LoginPageLocators.REGISTER_SUBMIT_BUTTON)
        register_submit_button.click()

