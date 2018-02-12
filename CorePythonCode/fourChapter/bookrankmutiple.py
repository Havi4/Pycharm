from atexit import register
from re import compile
from threading import Thread
from time import ctime
import urllib
import urllib.request


REGEX = compile('#([\d,]+) in Books')
AMZN = 'https://www.amazon.cn/dp/'
ISBNs = {
    '0132269937':'Core Python Programming',
}

def getRanking(isbn):
    page = urllib.request.urlopen('%s%s' %(AMZN, isbn))
    data = page.read()
    print('data:---%s' %data)
    page.close()
    list = REGEX.findall(data.decode('utf-8'))
    if len(list) > 0:
        return list[0]
    else:
        return 'not found'

def _showRanking(isbn):
    Thread(target=_showRanking, args=())
    # print('---%r ranked %s' %(ISBNs[isbn], getRanking(isbn)))

def _main():
    print('At : %s' %ctime() + 'on amazon')
    for isbn in ISBNs:
        _showRanking(isbn)

@register
def _atexit():
    print('all done:%s' %ctime())

if __name__ == '__main__':
    _main()