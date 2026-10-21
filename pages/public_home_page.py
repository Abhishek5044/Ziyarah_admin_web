import re

from playwright.sync_api import Page


class PublicHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.login_link = page.get_by_role("link", name=re.compile(r"log\s*in", re.IGNORECASE))
        self.newsletter_email_field = page.get_by_role("textbox", name="Your email address")
        self.newsletter_submit_button = page.locator(".newsletter button")
        self.newsletter_feedback = page.locator(
            ".newsletter [role='alert'], "
            ".newsletter .error, "
            ".newsletter .invalid-feedback"
        )
        self.app_feature_links = {
            name: page.get_by_role(
                "link", name=re.compile(rf"^{re.escape(name)}(?:\b|$)")
            )
            for name in (
                "Explore Mosque",
                "Learn More About Us",
                "Submit Donation",
                "Events",
                "Donations",
                "Live Events",
                "Community Chat",
                "Islamic Courses",
            )
        }
        self.app_modal_heading = page.get_by_role("heading", name="Get the App", exact=True)
        self.app_modal_close_button = page.get_by_role("button", name="Close", exact=True)

    def open_login(self) -> None:
        self.login_link.click()

    def submit_newsletter_email(self, email: str) -> None:
        self.newsletter_email_field.fill(email)
        self.newsletter_submit_button.click()

    def newsletter_email_has_type_mismatch(self) -> bool:
        return self.newsletter_email_field.evaluate(
            "(input) => input.validity.typeMismatch"
        )

    def open_app_feature(self, name: str) -> None:
        self.app_feature_links[name].click()

    def close_app_feature_modal(self) -> None:
        self.app_modal_close_button.click()

    def navigate_home(self) -> None:
        self.page.goto("https://demo-2.ziyarahalmasjid.com/#")
