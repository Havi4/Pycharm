import re
from random import random
aString = 'hi, i am Shirley Hilton, i am his wife.'
m = re.findall(r'hi', aString)
if m:
    print(m)

mb = re.findall(r'\bhi\b', aString)
if mb:
    print(mb)

mz = re.findall(r'[hi]', aString)
if mz:
    print(mz)

ma = re.findall(r'i.', aString)
if ma:
    print(ma)
mc = re.findall(r'.', aString)
mi = re.findall(r'i\S', aString)
print(mi)
# if mc:
#     print(mc)
#
# md = re.findall(r'\*', aString)
# print(md)
#
# mg = re.findall(r'i.*e', aString)
# print(mg)

myTestString = '我是Hello123,Haha'
re1 = re.findall(r'\w', myTestString)
print(re1)

re2 = re.findall(r'^h', aString)
print(re2)

print(random())