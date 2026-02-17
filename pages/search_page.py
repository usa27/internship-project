from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep

class SearchPage(Page):
    OFF_PLAN_BTN = (By.XPATH, '//span[text()="Off-plan"]')
    OFF_PLAN_HEADER = (By.XPATH, '//button[text()="Off-plan"]')
    FILTER_STATUS_BTN = (By.XPATH, '//button[text()="Status"]')
    OUT_OF_STOCK_STATUS_BTN = (By.CSS_SELECTOR, '[data-test-id="filter-badge-out_of_stock"]')
    FILTER_IS_ACTIVE_BTN = (By.CSS_SELECTOR, '[data-test-id="search-and-filters-button"]')
    OUT_OF_STOCK_TAG = (By.CSS_SELECTOR, '[data-test-id="project-card-sale-status"]')

    def click_off_plan(self):
        self.wait_until_element_present(*self.OFF_PLAN_BTN)
        side_menu_items = self.find_elements(*self.OFF_PLAN_BTN)
        side_menu_items[1].click()

    def filter_by_status_out_of_stock(self):
        self.wait_until_element_present(*self.FILTER_STATUS_BTN)
        filter_by_status = self.find_elements(*self.FILTER_STATUS_BTN)
        filter_by_status[1].click()
        self.wait_until_clickable_click(*self.OUT_OF_STOCK_STATUS_BTN)

    def verify_products_contain_status_tag(self):
        sleep(10)
        self.wait_until_element_present(*self.FILTER_IS_ACTIVE_BTN)
        self.wait_until_element_present(*self.OUT_OF_STOCK_TAG)
        status_tags = self.find_elements(*self.OUT_OF_STOCK_TAG)

        assert status_tags, "No status tags found"

        for status_tag in status_tags[:8]:
            each_tag = status_tag.text.strip()

            assert each_tag == "Out Of Stock", \
                f"Expected 'Out Of Stock' but got '{each_tag}'"
            print(f' {each_tag}')

    def verify_off_plan_opened(self):
        self.wait_until_element_present(*self.OFF_PLAN_HEADER)