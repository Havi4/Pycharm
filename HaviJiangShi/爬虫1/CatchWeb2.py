# this python is to improve the scrape to catch web
import re
import urllib.request
import urllib
from collections import deque
# use the queue to
queue = deque()
visited = set()
url = 'http://news.dbanotes.net'
queue.append(url)
cnt = 0

#
while queue:
    url = queue.popleft() #pop the header url to use
    visited |= {url}
    print('now is catch:' + str(cnt) + ' is catching ' + url)
    cnt += 1
    urlop = urllib.request.urlopen(url, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue
    try:
        data = urlop.read().decode('utf-8')
    except:
        continue
    linkre = re.compile('herf=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列: -->', +x)


# to show how to add header to request

urlOne = 'http://www.baidu.com'
reqOne = urllib.request.Request(urlOne, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})

oper = urllib.request.urlopen(reqOne)
data = oper.read()
print(data.decode('utf-8'))