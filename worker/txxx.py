import threading,time

def aa(xxx):
    print threading.current_thread().getName() +"\n"
    time.sleep(3)
    for i in range(xxx*2):
        print i

if __name__ == '__main__':
    lis = [1,2,3,4,5]
    th=[]
    for i in lis:
        thx = threading.Thread(target=aa,args=(i,))
        thx.start()
        th.append(thx)
    for i in th:
        i.join()