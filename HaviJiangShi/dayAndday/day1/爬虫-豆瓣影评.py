#coding:utf-8
#first, get data from douban
import urllib.request
from bs4 import BeautifulSoup as bs
import re
import jieba
import pandas as pd
import numpy
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from wordcloud import WordCloud#词云包

douban_url = 'https://movie.douban.com/nowplaying/hangzhou/'
douban_res = urllib.request.urlopen(douban_url)
html_data = douban_res.read().decode('utf-8')
# print(html_data)
soup = bs(html_data, 'html.parser')
nowplaying_movie = soup.find_all('div', id='nowplaying')
nowplaying_movie_list = nowplaying_movie[0].find_all('li', class_='list-item')
# print(nowplaying_movie_list)
nowplaying_list = []
for item in nowplaying_movie_list:
    nowplaying_dic = {}
    nowplaying_dic['id'] = item['data-subject']
    for tag_image_item in item.find_all('img'):
        nowplaying_dic['name'] = tag_image_item['alt']
        nowplaying_list.append(nowplaying_dic)

print(nowplaying_list)
comment_url = 'https://movie.douban.com/subject/%s/comments?start=0&limit=20'
request_url = comment_url %(nowplaying_list[1]['id'])
# print(request_url)
resp = urllib.request.urlopen(request_url)
resp_data = resp.read().decode('utf-8')
soup = bs(resp_data, 'html.parser')
comment_div_lists = soup.find_all('div', class_='comment')
# print(comment_div_lists)
eachCommentList = []
for item in comment_div_lists:
    if item.find_all('p')[0].string is not None:
        eachCommentList.append(item.find_all('p')[0].string)

# print(eachCommentList)
# 数据清洗
comments = ''
for k in range(len(eachCommentList)):
    comments = comments + (str(eachCommentList[k])).strip()
# print(comments)

pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, comments)
cleaned_comments = ''.join(filterdata)

segment = jieba.lcut(cleaned_comments)
words_df = pd.DataFrame({'segment': segment})
print(words_df.head())
stopwords = pd.read_csv('stop_words_zh_UTF-8.txt', index_col=False, quoting=3,sep='\t',names=['stopword'],encoding='utf-8')
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]
print(words_df.head())

words_stat = words_df.groupby(by=['segment'])['segment'].agg({'计数':numpy.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)

print(words_stat.head())

matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
#
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80)
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
#
word_frequence_list = []
for key in word_frequence:
    temp = {key: word_frequence[key]}
    word_frequence_list.append(temp)
print(word_frequence_list)
#
wordcloud = wordcloud.fit_words(word_frequence_list)
plt.imshow(wordcloud)








