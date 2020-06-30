import scrapy


class SosekiSpider(scrapy.Spider):
    name = 'soseki'  # Spiderの名前
    start_urls = [          # 取得対象のWebサイト
        'https://www.aozora.gr.jp/index_pages/person148.html'
    ]

    def parse(self, response):
        # 本文からタイトルを取得して表示
        title = response.css('title')
        print(title.extract())
