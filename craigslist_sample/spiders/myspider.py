from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from craigslist_sample.items import CraigslistSampleItem
from scrapy.http import Request
from urlparse import urljoin

class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/npo/"]

    def parse(self, response):
        base_url = "http://sfbay.craigslist.org/search/npo"
        url=response.xpath("//a[@class='button next']/@href")[0].extract()
        print "url================",url
        for sel in response.xpath("//a[@class='hdrlnk']"):
            craigsList = CraigslistSampleItem()
            craigsList['link'] = sel.xpath("@href").extract()
            craigsList['title'] = sel.xpath("text()").extract()
            yield craigsList
        yield Request(urljoin(base_url,url))
        
        
        