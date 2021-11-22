import threading


def worker(tid:int, lock:threading.Lock, nextLock: threading.Lock):
    i = 0
    isFirst = True
    while True:
        if isFirst and tid == 0:
            isFirst = False
        else:
            lock.acquire()
        print(f"{i}{tid}   线程id: {tid}")
        i+=1
        # lock.acquire()
        nextLock.release()

def print_in_order():
    lockList = []
    for _ in range(10):
        l = threading.Lock()
        # l.acquire(blocking=False)
        lockList.append(l)

    pool = []
    for i in range(10):
        t = threading.Thread(
            target=worker,
            kwargs={
                "tid": i,
                "lock": lockList[i], 
                "nextLock": lockList[(i+1)%10]
            }
        )
        pool.append(t)

    for t in pool:
        t.start()
        t.join()
    

if __name__ == "__main__":
    print_in_order()