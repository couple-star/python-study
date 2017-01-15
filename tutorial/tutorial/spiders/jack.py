# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy


class JackSpider(scrapy.Spider):
    name = "jack"

    def start_requests(self):
        urls = [

        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        m=response.css('div.ibox-content')
        page = response.url.split("/")[-2]
        # filename = 'quotes-%s.txt' % page
        with open('lists', 'ab') as f:
            f.write(page+'\n')
            for i in m:
                n=i.css('h2::text').extract_first().encode('utf-8')
                time=i.css('span.text-muted::text').extract_first().encode('utf-8')
                f.write('\t'+n+time+'\n')
        # self.log('Saved file %s' % filename)


