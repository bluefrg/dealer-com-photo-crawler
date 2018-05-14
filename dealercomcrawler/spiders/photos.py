# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.linkextractors import LinkExtractor

class PhotosSpider(scrapy.Spider):
    name = "photos"

    vdp_matcher = re.compile('\/(used|new)\/.+\.htm')

    vlp_matcher = re.compile('\/(used-inventory|new-inventory)\/')

    def __init__(self, domain='', **kwargs):
        self.start_urls = [domain]
        super().__init__(**kwargs)

    def parse(self, response):
        # Look for inventory listing pages
        for link in LinkExtractor(allow=self.vlp_matcher).extract_links(response):
            yield scrapy.Request(link.url, self.parse)

        # Look for vehicle details pages
        for link in LinkExtractor(allow=self.vdp_matcher).extract_links(response):
            yield scrapy.Request(link.url, self.parse)

        # Are we on a vehicle details page, if so parse it
        if self.vdp_matcher.search(response.url):
            yield {
                'vin': response.selector.css('.vin .value::text').extract_first(),
                'asking_price': response.selector.css('.internetPrice::attr(data-attribute-value)').extract_first(),
                'photos': response.selector.css('#photos a.js-link::attr(href)').extract()
            }
