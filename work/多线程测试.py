

'''

import threading,time
from selenium import webdriver

def run1(n):
    print('task1',n)
    time.sleep(2)
    # print(n)
    driver = webdriver.Chrome()
    time.sleep(3)
    driver.close()

def run2(n):
    print('task2',n)
    time.sleep(2)
    # print(n)
    driver = webdriver.Chrome()
    time.sleep(3)
    driver.close()

if __name__ == '__main__':
    t1 = threading.Thread(target=run1,args=('t1',))
    t2 = threading.Thread(target=run2,args=('t2',))
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

'''

#二次封装多线程类


import threading,time
from selenium import webdriver

class Mythread(threading.Thread):


    def __init__(self,n):
        # super(Mythread, self).__init__()
        threading.Thread.__init__(self)
        print('new_init方法')
        self.n = n


    def run(self) -> None:
        print('task1', self.n)
        time.sleep(2)
        # print(n)
        driver = webdriver.Chrome()
        time.sleep(3)
        driver.close()

t1 = Mythread('t1')
t1.setDaemon(True)
print('start')
t1.start()
t1.join()
print('end')




#线程共享资源--出现脏数据
# import threading
# import time
#
# g_num = 100
#
# def work1():
#     global g_num
#     for i in range(3000000):
#         g_num += 1
#     print("in work1 g_num is : %d" % g_num)
#
#
# def work2():
#     global g_num
#     # print("in work2 g_num is : %d" % g_num)
#     for i in range(3000000):
#         g_num += 1
#     print("in work2 g_num is : %d" % g_num)
#
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=work1)
#     t2 = threading.Thread(target=work2)
#     t1.start()
#     time.sleep(1)
#
#     t2.start()

#互斥锁

# from threading import Thread,Lock
# import os,time
#
#
# def work():
#     global n
#     lock.acquire()
#     temp=n
#     time.sleep(0.1)
#     n=temp-1
#     lock.release()
#
#
# if __name__ == '__main__':
#     lock=Lock()
#     n=100
#     l=[]
#     for i in range(100):
#         p=Thread(target=work)
#         l.append(p)
#         p.start()
#     for p in l:
#         p.join()

#
# import threading
# import time
#
# g_num = 100
#
# def work1():
#     lock.acquire()
#     global g_num
#     for i in range(3000000):
#         g_num += 1
#     lock.release()
#     print("in work1 g_num is : %d" % g_num)
#
#
# def work2():
#     lock.acquire()
#     global g_num
#     # print("in work2 g_num is : %d" % g_num)
#     for i in range(3000000):
#         g_num += 1
#     lock.release()
#     print("in work2 g_num is : %d" % g_num)
#
#
#
# if __name__ == '__main__':
#     lock = threading.Lock()
#     t1 = threading.Thread(target=work1)
#     t2 = threading.Thread(target=work2)
#     t1.start()
#     time.sleep(1)
#
#     t2.start()
