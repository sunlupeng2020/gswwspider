from selenium import webdriver
from lxml import etree

driver = webdriver.PhantomJS(executable_path=r'C:\Users\Administrator\phantomjs-2.1.1-windows\bin\phantomjs.exe')
# driver = webdriver.Chrome(executable_path="C:\\Program Files (x86)\\ChromeCore\\chromedriver.exe")
driver.get('http://47.95.10.46/problemset.php?p=1')
#

# driver.get('http://www.baidu.com/')
# timutr = driver.find_elements_by_xpath("//tbody/tr")
# timuid01s= timutr.xpath("./td[2]")
# print(timuid01s.text)

# 得到题目ID号
timuids = driver.find_elements_by_xpath("//tbody/tr/td[2]")
# 得到题目标题
timutitles = driver.find_elements_by_xpath("//tbody/tr/td[3]")
# 得到题目提交数，通过数，通过率
timutglvs = driver.find_elements_by_xpath("//tbody/tr/td[6]")
# 循环输出题目ID号
print(len(timuids)) # 输出49
print(timuids[2].text) #输出第二行的数据
# for timuid in timuids:
#     print(data.text)
# import urllib.requesta
# from lxml import etree
# import re
#
# headers ={
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# 'Cookie': 'PHPSESSID=vgj66jtksnmhq5e6ucelqkqjp7'
# }
#
# url = "http://acm.hi-54.com/problemset.php?p=1"
# request = urllib.request.Request(url, headers=headers)
# response = urllib.request.urlopen(request)
# html = response.read().decode("utf-8")
# root = etree.HTML(html)
#
#
# timuids = root.xpath("//*[@id='oj-ps-problemlist']/tr/td[2]/text()")
# print(timuids)
# print(root)
# print(html)

