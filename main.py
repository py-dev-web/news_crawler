from scrapers.base_scraper import BaseArticleScraper


with BaseArticleScraper() as scraper:
        scraper = scraper.create_child('abcn')
        article = scraper.scrape()