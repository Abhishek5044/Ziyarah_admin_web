from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_field = page.locator("#email")
        self.password_field = page.locator("#password")
        self.access_dashboard_button = page.get_by_role("button", name="Access Dashboard", exact=True)

    def sign_in(self, email: str, password: str) -> None:
        self.email_field.fill(email)
        self.password_field.fill(password)
        self.access_dashboard_button.click()
