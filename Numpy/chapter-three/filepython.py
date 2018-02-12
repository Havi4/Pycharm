import numpy as np
i1 = np.eye(2)
print(i1)
np.savetxt('eye.txt', i1)
# read the data from data.csv
(c, v) = np.loadtxt('data.csv', delimiter=',',usecols=(3, 6), unpack=True)
print('kai pan : %s, cheng jiao liang: %s' %(c, v))

vwap = np.average(c, weights=v)
print('vwap : %s' %vwap)
mean = np.mean(c)
# 说明了权重对数据的影响
print('mean: %s' %mean)
# 时间加权平均价格：时间月考后，对数据越重要
t = np.arange(len(c))
twap = np.average(c, weights=t)
print('twap is %s' %twap)
# 取值范围
# 首先读取所有的最高价和所有的最低价
(h, l) = np.loadtxt('data.csv', delimiter=',', usecols=(3, 4), unpack=True)
print('hight : %s' %np.max(h))
print('low: %s' %np.min(l))
print('最大值差值：%s' %np.ptp(h))
