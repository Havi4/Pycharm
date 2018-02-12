import threading
from time import sleep, ctime
loops = [2, 4]
class ThreadFunc(object):
    # 初始化方法
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)

def loop(nloop, nsec):
    print('start loop:%s at:%s' %(nloop, ctime()))
    sleep(nsec)
    print('end loop:%s at:%s' %(nloop, ctime()))

def main():
    print('thread start at:%s' %ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop,(i, loops[i]),loop.__name__))
        threads.append(t)

    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    print('all done')
if __name__ == '__main__':
    main()