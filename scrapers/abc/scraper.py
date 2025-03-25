from scrapers.base_scraper import BaseScraper

class ABCScraper(BaseScraper):
    def __init__(self, endpoint):
        super().__init__(endpoint)

    def scraping(self):
        pass


