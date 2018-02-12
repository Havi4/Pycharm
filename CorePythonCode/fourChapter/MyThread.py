import threading
from time import ctime
# 类的继承
class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def getResult(self):
        return self.res
    def run(self):
        print('start %s' %self.name)
        self.res = self.func(*self.args)
        print('finish done')