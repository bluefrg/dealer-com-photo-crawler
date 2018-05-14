# -*- coding: utf-8 -*-
from urllib.parse import urlparse

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DealercomcrawlerPipeline(object):
    def process_item(self, item, spider):

        # Dealer.com photo urls include params for sizing, nix em
        def clean_photo_url(url):
            x = urlparse(url)
            return x[0] + '://' + x[1] + x[2]

        item['vin']             = item['vin'].strip()
        item['asking_price']    = item['asking_price'].strip()
        if item['photos']:
            item['photos'] = list(map(clean_photo_url, item['photos']))

        return item

