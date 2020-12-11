from scrapy import cmdline
#cmdline.execute("scrapy crawl gsww_spider".split(" "))作用与下面两行相同：在本窗口中运行爬虫
cmds=["scrapy","crawl","gsww_spider"]
cmdline.execute(cmds)