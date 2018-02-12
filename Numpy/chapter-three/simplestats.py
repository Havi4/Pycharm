import numpy as np
# 读取收盘价
c = np.loadtxt('data.csv', delimiter=',', usecols=(2,), unpack=True)
print('medium is %s' %np.median(c))
c_sorted = np.msort(c)
print('sorted arr : %s' %c_sorted)

fangcha = np.var(c)
print('fangcha:%s' %fangcha)