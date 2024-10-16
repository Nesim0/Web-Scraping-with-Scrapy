from pathlib import Path
import scrapy
class QuotesSpider(scrapy.Spider):
    name = "books"
    page_count = 0
    start_urls = [
        "https://www.kitapyurdu.com/index.php?route=product/best_sellers&page=1&list_id=1"
    ]
    def parse(self, response):
        books_names= response.css("div.name.ellipsis a span::text").extract()
        books_authors= response.css("div.author span a span::text").extract()
        books_publisher= response.css("div.publisher span a span::text").extract()
        i=0
        while (i < len(books_names)):
            yield{
                "name": books_names[i],
                "authors": books_authors[i],
                "publisher": books_publisher[i]
            }
            i+=1
        next_url=response.css("a.next::attr(href)").extract_first()
        # self.page_count+=1
        if next_url is not None: #and self.page_count!=5
            yield scrapy.Request(url=next_url,callback=self.parse)
        else:
            pass
# response.css("name ellipsis::text").extract()[0] 0. index
# response.css("title::text").extract_first() 
# response.xpath("//title/text()").get()
# response.css("a.next::attr(href)").extract_first()    