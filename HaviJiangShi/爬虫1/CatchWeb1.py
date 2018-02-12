#encoding:UTF-8
# 简单的直接使用urllib去获取网页data数据，数据没有经过任何的处理
import urllib
import urllib.parse
import urllib.request
url = 'http://www.baidu.com'
data = urllib.request.urlopen(url).read()
data = data.decode('utf-8')
# print(data)
# we need to catch the jecay note web,you define search ruler for yourself
searchKey = {}
searchKey['word'] = 'havi'
url_value = urllib.parse.urlencode(searchKey)
baidu_url = 'http://www.baidu.com/s?'
baidu_search_url = baidu_url + url_value
searchData = urllib.request.urlopen(baidu_search_url).read()
searchData = searchData.decode('utf-8')
print(searchData)

