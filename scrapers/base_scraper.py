from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pickle
import os
import time
import importlib
from db.models.article import Article


class BaseArticleScraper(ABC):
    def __init__(self, proxy=None, session_file="session.pkl"):
        self.session_file = session_file
        self.proxy = proxy
        self.driver = self._initialize_driver()
        self._load_session()

    def _initialize_driver(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if self.proxy:
            options.add_argument(f"--proxy-server={self.proxy}")

        service = Service("chromedriver")
        driver = webdriver.Chrome(service=service, options=options)
        return driver

    def _load_session(self):
        if os.path.exists(self.session_file):
            with open(self.session_file, "rb") as f:
                cookies = pickle.load(f)
                self.driver.get("https://www.example.com")  # Load a base URL to set cookies
                for cookie in cookies:
                    self.driver.add_cookie(cookie)

    def _save_session(self):
        with open(self.session_file, "wb") as f:
            pickle.dump(self.driver.get_cookies(), f)

    def open_endpoint(self, url):
        try:
            self.driver.get(url)
            time.sleep(3)  # Dynamic delay before scraping
        except Exception as e:
            print(f"Error opening {url}: {e}")

    @abstractmethod
    def scrape(self) -> Article:
        """This method must be implemented in child classes"""
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._save_session()
        self.driver.quit()

    @staticmethod
    def create_child(origin: str):
        class_path = f"scrapers.{origin.lower()}.scraper.{origin.upper()}Scraper"
        module_name, class_name = class_path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        child_class = getattr(module, class_name)
        return child_class()