import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import ssl
# define an unzip func
ssl._create_default_https_context = ssl._create_unverified_context
def ungzip(data):
    try:#try to unzip,because some response need't unzip
        print('unziping....')
        data = gzip.decompress(data)
        print('unzip done!')
    except:
        print('no nedd to unzip data')
    return data

# define an re to match certificate
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]
# define header

def getOpener(head):
    # define cook
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Cookie': 'aliyungf_tc=AQAAAJ5a8E1+oAUA07CbtGExbMqNhb+O; q_c1=e42d3021c1f144bfa1816e1c0ff12208|1502171394000|1493102346000; _xsrf=7c9c0bb6-e04b-40a2-998d-4f0c21ad2fe3; z_c0="2|1:0|10:1502674230|4:z_c0|92:Mi4xVXYxZEFBQUFBQUFBSUlLUWtfaXBDeWNBQUFDRUFsVk5Ob3E0V1FEMmRqYWlhQzV1VEY1UkdrSDVzVjBCVjltdERR|bf21703dd86b5955bc0255466f8afee84eb4014aed12d9b16d73b27a853e263e"; __utma=51854390.157759261.1495928623.1502633054.1502674179.8; __utmv=51854390.000--|2=registration_date=20140526=1^3=entry_date=20170425=1; __utmz=51854390.1502674179.8.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; cap_id="YjA1YTE2YWZhOTY0NDZlMzkzMzMwNmI3YTMwYjczZGY=|1502674175|ce1bab7fd7bc374e1368ad24465ad5a681e20d7d"; l_cap_id="MDAyMDNiMzA4MGRhNDYzOTg2MzczZGIxNTlkODM5ZGQ=|1502674175|bf381cf08ea39fdc650b33f4880843268bfeaa13"; r_cap_id="YjAyOGQ0MDRiMjBhNGQxYzhhYmI3N2IwMGQ5YWQ1Nzg=|1502674175|5756b840983d45609e6e63c96babdd8b55d5eb4a"; q_c1=e42d3021c1f144bfa1816e1c0ff12208|1502171394000|1493102346000; _zap=39295dbb-6bda-4417-b50d-fd8a4e54b8ce; d_c0="ACCCkJP4qQuPTiZW6a8weQH4SXsyLt6SiIg=|1493165121"',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.1.1 Safari/603.2.4',
    'Accept-Language': 'en-us',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive'
}

url = 'http://www.zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)
print(data.decode('utf-8'))
_xsrf = getXSRF(data)
print(_xsrf)
