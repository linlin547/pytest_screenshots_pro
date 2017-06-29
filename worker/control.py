#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,threading,time
def control_test(com_exe):
    print threading.current_thread().getName() + "\n"
    print com_exe
    os.system(com_exe)

if __name__ == '__main__':
    os.system("cd /Users/xxx/Documents/pytest_product/worker")
    cmd_lis = ["pytest --browser=chrome --html=./chrome.html","pytest --browser=firefox --html=./firefox.html"]
    th_list = []
    for i in cmd_lis:
        th = threading.Thread(target=control_test,args=(i,))
        th.start()
        th_list.append(th)
    for n in th_list:
        n.join()

