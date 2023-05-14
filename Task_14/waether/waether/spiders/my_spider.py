import re
import logging

import scrapy
import pandas as pd


class MySpider(scrapy.Spider):
    name = 'test'
    start_urls = ['https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2']

    def parse(self, response):
        logging.info('Searching weather')
        weather_dict = {'data': [], 'min': [], 'max': []}
        items = response.css('.main')
        for item in items:
            weather_dict['data'].append(re.search(r'\d{4}-\d{2}-\d{2}',
                                                  item.css('.day-link::attr(data-link)').get()).group())
            weather_dict['min'].append(item.css('.min span::text').get())
            weather_dict['max'].append(item.css('.max span::text').get())
        yield weather_dict
        df = pd.DataFrame(weather_dict)
        df.to_excel('aboba.xlsx')
