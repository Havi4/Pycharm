from collections import deque
# python's queue ,you can create an queue with an array
queue = deque(['havi', 'li', 'wang'])
queue.append('dabai')
print(queue)
queue.pop()
print(queue)
queue.popleft()
print(queue)

# python's set: use {} or () to create an set, in the set, you can use
# to duplicate remove.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

if 'car' in basket:
    print('this element in this set')
else:
    print('no')
#
a = set('absdkflsdsdlkf')
b = set('abclkieieeowueio')
print(a)
print(b)
print(a | b)
print(a & b)
print(a ^ b)

