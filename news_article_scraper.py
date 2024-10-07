import scrapy

#creating spider class
class RandomSpider(scrapy.Spider):
    #creating a name for the spider and give the start url
    name = "random_spider"
    start_urls = [
        'https://economictimes.indiatimes.com/markets/stocks/news/iran-israel-war-how-it-may-impact-investors/articleshow/109369753.cms',  # Replace this with any website or blog
    ]

    def parse(self, response):
        # Extract title
        title = response.xpath('//title/text()').get()

        # Extract all paragraphs
        paragraphs = response.xpath('//p/text()').getall()

        # Extract headings (h1, h2, h3, etc.)
        headings = response.xpath('//h1/text() | //h2/text() | //h3/text()').getall()

        # Extract links
        links = response.xpath('//a/@href').getall()

        # Extract images
        images = response.xpath('//img/@src').getall()

        # Save and return the extracted data as a dictionary
        yield {
            'Title': title,
            'Paragraphs': paragraphs,
            'Headings': headings,
            'Links': links,
            'Images': images
        }

