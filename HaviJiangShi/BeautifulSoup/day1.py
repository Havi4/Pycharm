from bs4 import BeautifulSoup
import os
filemanager = open('ailisi.html', 'r')
html = filemanager.read()
soup = BeautifulSoup(html, 'html.parser')
print(soup.head.title)#一般来说只是获取第一个tag
# 获取html title;soup解析获取的是这个标签
print('title: %s' %soup.title)
print('title name: %s' %soup.title.string)
# find 只会从body找到第一个
print(soup.find('p'))
# 从一开始你要先确定tag系列，
tagp = soup.p
print(tagp['class'])
print(tagp.string)

markup = '<b><!hye this is an comment?--></b>'
soup1 = BeautifulSoup(markup, 'html.parser')
comment = soup1.b.string
print(comment)

print(soup.find(string = 'the dormouses story'))
print(tagp.find('b'))