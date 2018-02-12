#从 url中过滤出所有的直播的ids
import requests
from bs4 import BeautifulSoup
import re

# 过滤所有的liveid
def filterLiveIds(url):
    html = requests.get(url).text
    liveIds = set()#避免重复，这个是set
    bsObjc = BeautifulSoup(html, 'html.parser')
    # print('All Obj: %s' %bsObjc.findAll('a', href=re.compile('^(/l/)')))
    for link in bsObjc.findAll('a', href=re.compile('^(/l/)')):
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            liveId = re.findall('[0-9]+', newPage)
            liveIds.add(liveId[0])
    return liveIds

# print(filterLiveIds('http://www.huajiao.com/category/1000'))

#
def getUserId(liveId):
    html = requests.get('http://www.huajiao.com/' + 'l/' + str(liveId)).text
    bsObjc = BeautifulSoup(html, 'html.parser')
    text = bsObjc.title.get_text()
    res = re.findall('[0-9]+', text)
    return res[0]

print(getUserId(filterLiveIds('http://www.huajiao.com/category/1000').pop()))

# 获取主播的个人信息
def getUserData(userId):
    html = requests.get('http://www.huajiao.com/user/' + str(userId)).text
    bsObjc = BeautifulSoup(html, 'html.parser')
    data = dict()#define an set to
    try:
        userInfoObj = bsObjc.find('div', {'id': 'userInfo'})
        data['FAvatar'] = userInfoObj.find("div", {"class": "avatar"}).img.attrs['src']
        userId = userInfoObj.find("p", {"class": "user_id"}).get_text()
        data['FUserId'] = re.findall("[0-9]+", userId)[0]
        tmp = userInfoObj.h3.get_text('|', strip=True).split('|')
        # print(tmp[0].encode("utf-8"))
        data['FUserName'] = tmp[0]
        data['FLevel'] = tmp[1]
        tmp = userInfoObj.find("ul", {"class": "clearfix"}).get_text('|', strip=True).split('|')
        data['FFollow'] = tmp[0]
        data['FFollowed'] = tmp[2]
        data['FSupported'] = tmp[4]
        data['FExperience'] = tmp[6]
        return data
    except AttributeError:
        # traceback.print_exc()
        print(str(userId) + ":html parse error in getUserData()")
        return 0

    userid = getUserId(filterLiveIds('http://www.huajiao.com/category/1000').pop())
print(getUserData(29070021))

