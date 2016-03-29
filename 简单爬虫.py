#encoding:UTF-8
#简单爬虫
import urllib.request
import re

url = "http://wenku.it168.com/list/database_oracle_0_0_0_0_0_0_0_1.shtml"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
r = r'<a .*?>(.*?)[\s\S]</a>'
lists = re.findall(r,data)
print(lists)
