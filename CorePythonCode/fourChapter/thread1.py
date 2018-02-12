import threading
from time import sleep, ctime
loops = [2, 4]
def loop(nloop, nsec):
    print('start loop: %s at %s' %(nloop, ctime()))
    sleep(nsec)
    print('end loop: %s at %s' %(nloop, ctime()))

def main():
    print('starting at:%s' %ctime())
    threads = []
    nloops = range(len(loops))
    # here use for to create two thread
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    # here you must to start those thread
    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    print('all thread done')
if __name__ == '__main__':
    main()