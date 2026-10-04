import pytest
from playwright.sync_api import expect
from pages.homepage import HomePage
from pages.loginpage import LoginPage
from pages.adminpage import AdminPage
from config import Config
import time

def test_invalid_user_login(page):

    home_page = HomePage(page)
    logn_page = LoginPage(page)

    home_page.click_login()


    logn_page.set_email(Config.invalid_email)
    logn_page.set_login_password(Config.invalid_password)
    logn_page.click_login_button()

    time.sleep(3)
    error_msg = logn_page.get_login_error()
    expect(error_msg).to_be_visible(timeout=3000)


def test_valid_user_login(page):

    home_page = HomePage(page)
    logn_page = LoginPage(page)
    admin_page = AdminPage(page)

    home_page.click_login()


    logn_page.set_email(Config.email)
    logn_page.set_login_password(Config.password)
    logn_page.click_login_button()

    title = admin_page.get_page_title()
    expect(title).to_be_visible()