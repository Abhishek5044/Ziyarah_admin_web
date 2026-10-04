from playwright.sync_api import Page

class HomePage:
    """Page Object Model class for the 'Home' page."""
    #constructor should have only locators.
    def __init__(self, page: Page):
        """
        Constructor to initialize the Playwright page object
        and define all necessary locators.
        """
        self.page = page

        # ===== Locators =====
        # Using Playwright's 'locator' method to identify UI elements
        
        self.login_btton = page.locator('a:has-text("Login")')
        self.view_schedule_btton = page.locator('.btn.btn-outline-gold')
        self.prayer_times_btton = page.locator("div[class='hero-ctas'] a[class='btn btn-gold']")
        self.explore_mosque_btton = page.locator(".btn.btn-outline-light.store-trigger")
        
        

    # ===== Action Methods =====
    # Each method represents a user interaction on the page

    def get_home_page_title(self) -> str:
        """Return the title of the Home Page."""
        title = self.page.title()
        return title

    def click_login(self):
        try:
            self.login_btton.click()
        except Exception as e:
            print(f" Exception while clicking 'Login button': {e}")
            raise


    def click_view_schedule(self):
        try:
            self.view_schedule_btton.click()
        except Exception as e:
            print(f" Exception while clicking 'View Schedule button': {e}")
            raise

    def click_prayer_times(self):
        """Enter the product name into the search input box."""
        try:
            self.prayer_times_btton.click()
        except Exception as e:
            print(f" Exception while clicking 'Prayer times button': {e}")
            raise

    def click_explore_mosque(self):
        try:
            self.explore_mosque_btton.click()
        except Exception as e:
            print(f" Exception while clicking 'Explore Mosque' button: {e}")
            raise

