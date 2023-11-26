"""
Copyright (c) 2021 Rohan Shah
This code is licensed under MIT license (see LICENSE.MD for details)

@author: Slash
"""

# package imports
from datetime import datetime
import requests
from ebaysdk.finding import Connection
from threading import Thread

# local imports
from src.formattr import formatTitle

# configs
WALMART = {
    'site': 'walmart',
    'url': 'https://www.walmart.com/search?q=',
    'item_component': 'div',
    'item_indicator': {
        'data-item-id': True
    },
    'title_indicator': 'span.lh-title',
    'price_indicator': 'div.lh-copy',
    'link_indicator': 'a',
    'rating_indicator': 'div.flex.items-center.mt2 span.w_iUH7',
    'img_indicator': 'div.relative.overflow-hidden img'
}

'''AMAZON = {
    'site': 'amazon',
    'url': 'https://www.amazon.com/s?k=',
    'item_component': 'div',
    'item_indicator': {
        'data-component-type': 's-search-result'
    },
    'title_indicator': 'h2 a span',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal'
}

COSTCO = {
    'site': 'costco',
    'url': 'https://www.costco.com/CatalogSearch?dept=All&keyword=',
    'item_component': 'div',
    'item_indicator': {
        'class': 'product-tile-set'
    },
    'title_indicator': 'span a',
    'price_indicator': 'div.price',
    'link_indicator': 'span.description a',
}'''

BESTBUY = {
    'site': 'bestbuy',
    'url': 'https://www.bestbuy.com/site/searchpage.jsp?st=',
    'item_component': 'li',
    'item_indicator': {
        'class': 'sku-item'
    },
    'title_indicator': 'h4.sku-title a',
    'price_indicator': 'div.priceView-customer-price span',
    'link_indicator': 'a.image-link',
    'img_indicator': 'div.shop-sku-list-item div div a img'
}


# individual scrapers
class scrape_target(Thread):
    def __init__(self, query):
        self.result = {}
        self.query = query
        super(scrape_target,self).__init__()

    def run(self):
        """Scrape Target's api for data

        Parameters
        ----------
        query: str
            Item to look for in the api

        Returns
        ----------
        items: list
            List of items from the dict
        """

        api_url = 'https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1'

        page = '/s/' + self.query
        params = {
            'key': 'ff457966e64d5e877fdbad070f276d18ecec4a01',
            'channel': 'WEB',
            'count': '24',
            'default_purchasability_filter': 'false',
            'include_sponsored': 'true',
            'keyword': self.query,
            'offset': '0',
            'page': page,
            'platform': 'desktop',
            'pricing_store_id': '3991',
            'useragent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0',
            'visitor_id': 'AAA',
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',  # noqa: E501
            'Accept-Encoding': 'gzip, deflate',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '0',
            'Cache-Control': 'no-cache'
        }
        data = requests.get(api_url, params=params, headers=headers).json()

        items = []
        if data["data"]:
            for p in data['data']['search']['products']:
                item = {
                    'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    'title': formatTitle(p['item']['product_description']['title']),
                    'price': '$' + str(p['price']['reg_retail']),
                    'website': 'target',
                    #'link': shorten_url(p['item']['enrichment']['buy_url'])
                    'link': p['item']['enrichment']['buy_url'],
                    'img_link': p['item']['enrichment']['images']['primary_image_url'],
                    # 'rating': p['ratings_and_reviews']['statistics']['rating']['average']
                }
                items.append(item)

        self.result = items

class scrape_ebay(Thread):
    def __init__(self, query):
        self.result = {}
        self.query = query
        super(scrape_ebay,self).__init__()

    def run(self):
        """Scrape Target's api for data

        Parameters
        ----------
        query: str
            Item to look for in the api

        Returns
        ----------
        items: list
            List of items from the dict
        """

        EBAY_APP = 'BradleyE-slash-PRD-2ddd2999f-2ae39cfa'

        try:
            api = Connection(appid=EBAY_APP, config_file=None, siteid='EBAY-US')
            response = api.execute('findItemsByKeywords', {'keywords': self.query})
        except ConnectionError as e:
            print(e)
            self.result = []

        data = response.dict()

        items = []
        for p in data['searchResult']['item']:
            item = {
                    'timestamp': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
                    'title': formatTitle(p['title']),
                    'price': '$' + p['sellingStatus']['currentPrice']['value'],
                    'website': 'ebay',
                    #'link': shorten_url(p['viewItemURL'])
                    'link': p['viewItemURL'],
                    'img_link': p['galleryURL']
                }

            items.append(item)
            

        self.result = items


# CONFIGS = [WALMART, AMAZON, COSTCO, BESTBUY]
CONFIGS = [WALMART, BESTBUY]
