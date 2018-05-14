

# Dealer.com Photo Crawler

All clients of the Dealer.com platform use a similar format to their web structure, this Scrapy spider will crawl a domain passed in and provide an exported CSV file of a VIN and list of photo urls.

## Example Usage

`scrapy crawl photos -a domain=https://www.birchwood.ca/`