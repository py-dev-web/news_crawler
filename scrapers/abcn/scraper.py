from scrapers.base_scraper import BaseArticleScraper
from db.models.article import Article


class ABCNScraper(BaseArticleScraper):
    def scrape(self) -> Article:
        try:
            title = self.driver.find_element("xpath", "//h1").text
            endpoint_id =self.driver.find_element("xpath", "//h1").text
            identifier = self.driver.find_element("xpath", "//h1").text
            body = self.driver.find_element("xpath", "//h1").text
            link = self.driver.find_element("xpath", "//h1").text
            author = self.driver.find_element("xpath", "//h1").text
            published_at = self.driver.find_element("xpath", "//h1").text

            return Article(title=title, endpoint_id=endpoint_id, identifier=identifier,
                           body=body, link=link, author=author, published_at=published_at)
        except Exception as e:
            print(f"Error scraping data: {e}")
            return None


