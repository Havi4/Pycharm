import numpy as np
# numpy中的对象由两部分组成
# 2.1
# 创建一个数组
a = np.arange(5)
print('a: %s' %a)
c = np.arange(5)
b = np.array([a])
print('b: %s, b维度：%s' %(b, b.shape))
d = np.arange(24).reshape(2,3,4)
print(d)

a1 = np.arange(9).reshape(3,3)
a2 = a1 * 2
a3 = np.hstack((a1, a2))
print(a3)
a4 = np.vstack((a1, a2))
print(a4)
a5 = np.concatenate((a1, a2), axis=0)
print(a5)

b1 = np.column_stack((a1, a2))
print(b1)

c = np.arange(9).reshape(3,3)
print(c)
c1 = np.hsplit(c, 3)
print(c1)

d = np.arange(64).reshape(4,4,4)
print(d)
d1 = d*2
d2 = np.column_stack((d, d1))
d3 = np.vstack((d, d1))
print(d2)
print('**********')
print(d3)