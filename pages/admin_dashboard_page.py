import re

from playwright.sync_api import Page


class AdminDashboardPage:
    def __init__(self, page: Page):
        self.page = page
        self.welcome_heading = page.get_by_role("heading", name=re.compile(r"welcome back", re.IGNORECASE))
        self.sidebar_toggle_button = page.get_by_role("button", name="Toggle sidebar")
        self.section_buttons = {
            name: page.get_by_role("button", name=name, exact=True)
            for name in ("Access Control", "Prayers", "Notifications", "Events", "Community Hub")
        }
        self.account_menu_button = page.get_by_role("button", name=re.compile(r"\bAdmin$"))
        self.logout_button = page.get_by_role("button", name=re.compile(r"^log\s*out$", re.IGNORECASE))

    def click_sidebar_toggle(self) -> None:
        self.sidebar_toggle_button.click()

    def click_section(self, name: str) -> None:
        self.section_buttons[name].click()

    def open_admin_menu(self) -> None:
        self.account_menu_button.click()

    def log_out(self) -> None:
        self.logout_button.click()
