#coding:utf-8

'''
python提供了两个模块来实现多线程thread 和threading ，Thread 有一些缺点，在threading 得到了弥补
补充：Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，
对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。
'''

import threading

def thread1():
    for i in range(100):
        print "thread-----1--:" + str(i)

def thread2():
    for i in range(100):
        print "thread-----2--:" + str(i)

# thread1()
# thread2()

#启动线程
threading.Thread(target=thread1).start()
threading.Thread(target=thread2).start()










