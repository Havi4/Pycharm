import re
m = re.match('foo', 'ffoo_foo')
if m is not None:
    print(m.group())

#就像是类方法和实例方法
# match 方法是从开始匹配，如果匹配不到失败
m = re.search('foo', 'seafood_food')
if m is not None:
    print(m.group())
# 使用|匹配多个字符串

bt = 'bat|bet|bit'
m = re.match(bt, 'bat')
if m is not None:
    print(m.group())

m = re.match(bt, 'blt')
if m is not None:
    print(m.group())
# match是从进行匹配
m = re.match(bt, 'hi bit me!')
if m is not None:
    print(m.group())

m = re.search(bt, 'hi bit me!')
if m is not None:
    print(m.group())

# .可以匹配除换行意外的任何字符
anyend = '.end'
m = re.match(anyend, 'bend')
if m is not None:
    print(m.group())

# .
# 如果有特殊的字符需要用\来转义
pattarn = '3\.14'
m = re.match(pattarn, '3.14')
if m is not None:
    print(m.group())

# []是用来表示匹配集的
m = re.match('[cr][23][dp][o2]', 'c3po')
if m is not None:
    print(m.group())

# *******************************************
# 重复、特殊字符以及分组
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt, 'noboday@s.ss.com').group())

# ()是用来进行子组匹配的、、、（）用来定义子组的
m = re.match('(\w\w\w)-(\d\d\d)', 'abc-123')
print(m.group())
print(m.group(1))

# *******************************************
# 使用search时候，操作字符串的起始位置
m = re.search('^the', 'a the end')
if m is not None:
    print(m.group())
#         这个说明了必须从开始进行匹配

m = re.search(r'\bthe', 'bite the dog')
if m is not None:
    print(m.group())
#     r表示？？

# *******************************************
# findall and finditer
# findall返回的是一个数组
print(re.findall('car', 'car_car'))



# ******************************************
# sub() and subn()

a = re.sub('X', 'nihao', 'ha X dkaldk')
print(a)

a = re.subn('X', 'back to num', 'X ha this is an X')
print(a)



















