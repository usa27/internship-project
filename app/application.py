from pages.base_page import Page
from pages.sign_in_page import SignInPage
from pages.search_page import SearchPage

class Application:

    def __init__(self, driver):

        self.base_page = Page(driver)
        self.sign_in_page = SignInPage(driver)
        self.search_page = SearchPage(driver)