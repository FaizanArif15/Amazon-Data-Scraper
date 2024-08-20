import scrapy
from scraper_api import ScraperAPIClient

client = ScraperAPIClient('ABC')


class AmazonItemsSpider(scrapy.Spider):
    name = "amazon_items"
    allowed_domains = ["www.amazon.com"]
    start_urls = ["https://www.amazon.com/s?i=specialty-aps&bbn=16225007011&rh=n%3A16225007011%2Cn%3A193870011&ref=nav_em__nav_desktop_sa_intl_computer_components_0_2_6_3"]
    
    def parse(self, response):
        # pass
        
        products = response.css('div.s-result-item')
        for product in products:
            name = product.css('span.a-text-normal::text').get()
            # print(name)
            if name:
                # continue
                try:
                    rating = product.css('span.a-icon-alt::text').get().split(' ')[0]
                except:
                    rating = 'Not Yet'
                price = product.css('span.a-price-whole::text').get()
                
                yield{
                    'Name': name,
                    'Rating': rating,
                    'Price': price,
                }