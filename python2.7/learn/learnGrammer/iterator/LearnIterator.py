#coding:utf-8

'''
python迭代器的学习
'''

import os
curdir = os.path.split(os.path.realpath(__file__))[0]
myMap = {"name":"lili","age":27,"sex":"girl"}
myList = ["lili","lilei","hanmeimei","mica"]
myTuple = ("haha","hi","hello","你好")
myStr = "1234567"
fil = open(curdir + "/test.txt","r")

for i in myMap:
    print i
print "-----------------------"
for i in myList:
    print i
print "-----------------------"
for i in myTuple:
    print i
print "-----------------------"
for i in myStr:
    print i
print "-----------------------"
for i in fil:
    print i
fil.close()

