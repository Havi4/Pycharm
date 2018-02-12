import time
import random
starTime = time.time()
print('start time: %f' %starTime)
for i in range(1, 10):
    print(i)
endTime = time.time()
print('end time: %f' %endTime)
print('total time: %f' %(endTime - starTime))

def func(arg1 = 2, arg2 = 3):
    print(arg1, arg2)

func(1)
func(4, 5)

def func1(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)

func1(1,2)