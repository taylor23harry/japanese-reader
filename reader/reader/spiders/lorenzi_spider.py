import scrapy
import json

from glom import glom


class LorenziSpider(scrapy.Spider):
    name = "LorenziSpider"

    def start_requests(self):
        url = 'https://jisho.hlorenzi.com/api/v1/search'
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Content-Type': 'application/json; charset=utf-8'
        }

        body = {
            "query": "バカじゃないの。私は女狐じゃないです",
            "limit":10
        }

        request = scrapy.Request(
            method='POST',
            url=url,
            headers=headers,
            body=json.dumps(body),
            callback=self.parse
        )
        
        yield request
    
    def parse(self, response):
        data = json.loads(response.body.decode())

        json_sections = glom(data, 'entries')
        current_section = None
        for section in json_sections:
            section_type = glom(section, 'section')
            if section_type:
                current_section = section_type
                continue

            if current_section == ''

