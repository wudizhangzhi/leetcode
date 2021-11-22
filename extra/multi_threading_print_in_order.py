import threading


def worker(tid:int, lock:threading.Lock, nextLock: threading.Lock):
    i = 0
    while True:
        lock.acquire()
        print(f"{i}{tid}   线程id: {tid}")
        i+=1
        lock.acquire()
        nextLock.release()

def print_in_order():
    lockList = []
    for _ in range(10):
        l = threading.Lock()
        lockList.append(l)

    pool = []
    for i in range(10):
        t = threading.Thread(
            target=worker,
            args=(lockList[i], lockList[(i+1)%10])
        )
        pool.append(t)

    lockList[0].release()
    for t in pool:
        t.start()
        t.join()

if __name__ == "__main__":
    print_in_order()