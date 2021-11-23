import threading


Lock_list = list()
IsRunning = True

def worker(tid:int):
    global Lock_list, IsRunning
    i = 0
    while IsRunning:
        if Lock_list[tid]:
            print(f"{i*10+tid}   线程id: {tid}")
            if i*10+tid > 10000:
                IsRunning = False
                break
            i+=1
            Lock_list[tid] = False
            Lock_list[(tid+1)%10] = True

def print_in_order():
    global Lock_list
    for i in range(10):
        # l = threading.Lock()
        # # l.acquire(blocking=False)
        # lockList.append(l)
        if i==0:
            Lock_list.append(True)
        else:
            Lock_list.append(False)
    pool = []
    for i in range(10):
        t = threading.Thread(
            target=worker,
            kwargs={
                "tid": i,
            }
        )
        pool.append(t)
        t.start()

    for t in pool:
        t.join()

if __name__ == "__main__":
    print_in_order()