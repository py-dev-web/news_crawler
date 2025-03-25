from playwright.sync_api import sync_playwright
from abc import ABC, abstractmethod

class BaseScraper(ABC):
    def __init__(self, url):
        self.url = url
        self.browser = None
        self.page = None

        self.start_browser()
        self.open_links(url)

    def start_browser(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.page = self.browser.new_page()

    def close_browser(self):
        if self.browser:
            self.browser.close()

    def open_links(self, href):
        self.page.goto(href)

    @abstractmethod
    def scraping(self):
        pass

