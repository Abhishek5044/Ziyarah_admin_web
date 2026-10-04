from playwright.sync_api import Page, expect

class AdminPage:

    def __init__(self, page:Page):
        self.page = page

        self.page_title = page.locator("h2[class='mt-3 text-xl sm:text-2xl font-bold text-white']")



    def get_page_title(self):
        try:
            return  self.page_title 
        except Exception as e:
            print(f" Exception while fetching page title : {e}")
            return None



