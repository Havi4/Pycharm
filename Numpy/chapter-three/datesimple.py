import numpy as np
import datetime
# (dates, close) = np.loadtxt('data.csv', delimiter=',', usecols=(0, 1), unpack=True)
# print('dates: %s ；close: %s' %(dates, close) )
# unpack :是将数组中的内容分包；
def dateFormatter(b):
    a = str(b, encoding='utf-8')
    return datetime.datetime.strptime(a,'%Y-%m-%d').date().weekday()

(date2, close2) = np.loadtxt('data.csv', delimiter=',', usecols=(0, 1),converters={0:dateFormatter},unpack=True)
print('dates: %s' %date2)
