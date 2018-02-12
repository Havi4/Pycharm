from MyThread import MyThread
from time import ctime, sleep
def fib(x):
    sleep(0.5)
    if x < 2:
        return 1
    return (fib(x-2) + fib(x-1))

def fac(x):
    sleep(0.1)
    if x < 2:
        return 1
    return (x * fac(x-1))

def sum(x):
    sleep(0.1)
    if x<2:
        return 1
    return (x + sum(x-1))

funcs = [fib, fac, sum]
n = 3

def main():
    nfuncs = range(len(funcs))
    print('*****单线程开始****')
    for i in nfuncs:
        print('starting %s at: %s' %(funcs[i].__name__,ctime()))
        print(funcs[i](n))
        print('end %s at%s'%(funcs[i].__name__,ctime()))

    print('mutiple threads')
    threads = []
    for i in nfuncs:
        t = MyThread(funcs[i],(n,), funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].getResult())
    print('all done')

if __name__ == '__main__':
    main()