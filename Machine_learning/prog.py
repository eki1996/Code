# -*- coding: utf-8 -*-
import scrapy
class MyScap(scrapy.Spider):
    name="comment"
    start_urls=["https://www.babelio.com/auteur/Frederic-Dard/7187/citations"]
    
    def parse(self, response):
        for citation in response.css("div.post_con div.text.row div "):
            yield{'citation': citation.css('div ::text').extract_first()}
