from pages.base_page import Page
from selenium.webdriver.common.by import By

class SignInPage(Page):
    SIGN_IN_PAGE_HEADER = (By.XPATH, "//h1[text()='Sign in or create new account']")
    EMAIL_TEXTBOX = (By.ID, 'email-2')
    PASSWORD_TEXTBOX = (By.ID, 'field')
    CONTINUE_BTN = (By.XPATH, "//a[text()='Continue']")

    test_user_email = 'alexandrabugaeva1315@gmail.com'
    test_user_password = '*******'

    def verify_sign_in_page_opened(self):
        self.wait_until_element_present(*self.SIGN_IN_PAGE_HEADER)
        self.verify_url_contains('sign-in')
        expected_partial_text = 'Sign in or create new account'
        self.verify_partial_text(expected_partial_text, *self.SIGN_IN_PAGE_HEADER)

    def enter_valid_email(self):
        self.wait_until_element_present(*self.EMAIL_TEXTBOX)
        self.input_text(self.test_user_email, *self.EMAIL_TEXTBOX)

    def enter_valid_password(self):
        self.wait_until_element_present(*self.PASSWORD_TEXTBOX)
        self.input_text(self.test_user_password, *self.PASSWORD_TEXTBOX)

    def click_continue(self):
        self.wait_until_clickable_click(*self.CONTINUE_BTN)