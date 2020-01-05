import scrapy

class LiveMintSpider(scrapy.Spider):
    #Name of the spider
    name ="LiveMint_spider"
    allowed_urls = ['https://www.livemint.com/companies']

    def parse(self,response):
        #HTML div class name that we want to extract the data from
        SET_SELECTOR = '.itemListElement'
        #save all the content
        for livemint in response.css(SET_SELECTOR):
            pass