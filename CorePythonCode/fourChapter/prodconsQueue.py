from random import randint
from time import sleep
import queue
from MyThread import MyThread

def writeQ(myqueue):
    print('producing object for Q。。。。')
    myqueue.put('xxx', 1)
    print('size now:%s' %myqueue.qsize())

def readQ(myqueue):
    val = myqueue.get(1)
    print('consumed object from Q')

