import pytest
from playwright.sync_api import Page, expect
from pages.homepage import HomePage


def test_clicking_ui_elements(page):

    homepage = HomePage(page)

    expect(homepage.view_schedule_btton).to_be_visible()
    expect(homepage.view_schedule_btton).to_be_enabled()
    homepage.click_view_schedule()
  


    # expect(homepage.explore_mosque_btton).to_be_visible()
    # expect(homepage.explore_mosque_btton).to_be_enabled()
    # homepage.click_explore_mosque()

    expect(homepage.prayer_times_btton).to_be_visible()
    expect(homepage.prayer_times_btton).to_be_enabled()
    homepage.click_prayer_times()
    expect(page).to_have_url("https://demo-2.ziyarahalmasjid.com/#timings")