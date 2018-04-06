import scrapy
from ..items import BilibliItem
class MiyuSpider(scrapy.Spider):
    name = "Ganji"
    start_urls = ["http://bj.ganji.com/fang5/"]

    def parse(self, response):
        # print(response)
        Ganji = BilibliItem()
        price_list = response.xpath('//*[@class="f-list-item ershoufang-list"]/dl/dd[5]/div[1]/span[1]/text()').extract()
        title_list = response.xpath('//*[@class="f-list-item ershoufang-list"]/dl/dd[1]/a/text()').extract()
        for i,j in zip(title_list,price_list):
            Ganji['title']=i
            Ganji['money']=j
            yield Ganji#生成一个迭代器