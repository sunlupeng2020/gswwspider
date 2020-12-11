import scrapy


class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org']
    def myprint(self,value):
        print("="*30)
        print(value)
        print("="*30)

    def parse(self, response):
        self.myprint(type(response))
