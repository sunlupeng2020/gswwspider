import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import Selector
from ..items import GswwItem

class GswwSpiderSpider(scrapy.Spider):
    name = 'gsww_spider'
    allowed_domains = ['gushiwen.org']
    start_urls = ['https://www.gushiwen.org']
    def myprint(self,value):
        print("="*30)
        print(value)
        print("="*30)

    def parse(self, response):
        # self.myprint(type(response))
        gsw_divs = response.xpath("//div[@class='left']/div[@class='sons']")
        for gsw_div in gsw_divs:
            title = gsw_div.xpath('.//b/text()').get()
            # self.myprint(title)
            source = gsw_div.xpath(".//p[@class='source']/a/text()").getall()
            author = source[0]
            dynasty = source[1]
            # self.myprint(title)
            # self.myprint(author)
            # self.myprint(dynesty)
            # self.myprint("dynesty":dynesty,"author":author)
            content_list = gsw_div.xpath(".//div[@class='contson']//text()").getall()
            content = "".join(content_list).strip() #strip()用于去掉空格？
            item = GswwItem(title=title, author=author, dynasty=dynasty, content=content)
            yield item

            # self.myprint(contents)
