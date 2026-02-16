from behave import given, when, then
from time import sleep

@given('Open Reelly main page')
def open_main(context):
    context.app.base_page.open_url()


@when('Log in to the account')
def login_to_account(context):
    context.app.sign_in_page.verify_sign_in_page_opened()
    context.app.sign_in_page.enter_valid_email()
    context.app.sign_in_page.enter_valid_password()
    context.app.sign_in_page.click_continue()


@when('Click on “off plan” in the left side menu')
def click_off_plan(context):
    context.app.search_page.click_off_plan()


@when('Filter by status of “Out of Stocks”')
def filter_by_status(context):
    context.app.search_page.filter_by_status_out_of_stock()


@then('Verify the correct page opened')
def verify_off_plan_opened(context):
    context.app.search_page.verify_off_plan_opened()


@then('Verify each product contains the Out of Stocks tag')
def verify_products_contain_status_tag(context):
    context.app.search_page.verify_products_contain_status_tag()