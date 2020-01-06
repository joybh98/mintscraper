import scrapy

class LiveMintSpider(scrapy.Spider):
    #Name of the spider
    name ="LiveMint_spider"
    allowed_urls = ['https://www.livemint.com/companies']

    def parse(self,response):
        article['title'] = response.xpath('//div[@class="figcaption"]/text()').extract()