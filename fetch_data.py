import scrapy
from scrapy.crawler import CrawlerProcess

#setting the filename of the text file
filename = "fetched_text"

#creating a clean text file
with open(filename, 'wb') as f:
	f.write("")

class SoapItem(scrapy.Item):
	text = scrapy.Field()

class SoapSpider(scrapy.Spider):
	name = "soap"
	allowed_domains = ["tvmegasite.net"]
	start_urls = [
	"http://tvmegasite.net/transcripts/days/older/2016/trans-da-01-04-16.shtml",
	"http://tvmegasite.net/transcripts/days/older/2016/trans-da-01-05-16.shtml"

	]

	def parse(self,response):
		#for sel in response.xpath('//p'):
		#	item = SoapItem()
		#	item['text'] = sel.xpath('//p/text()').extract()
		
		#yield item
		item = (response.xpath('//p/text()').extract())
		clean_item = "".join(item)
		clean_item = clean_item.encode("utf8","replace")
		clean_item = clean_item.replace("\\r","")
		clean_item = clean_item.replace("\\n","")
		clean_item = clean_item.replace("u'","")
		clean_item = clean_item.replace('u"',"")

		with open(filename,'ab') as f:
			f.write(clean_item)


#Starting the Crawler
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(SoapSpider)
process.start() # the script will block here until the crawling is finished
