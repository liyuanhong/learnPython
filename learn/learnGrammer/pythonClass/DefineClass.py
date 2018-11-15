#coding:utf-8
#学习定义一个python类

class DefineClass1:
    def prt(self):
        for i in range(20):
            print i

#实例化一个python类
cls = DefineClass1()
cls.prt()
print "---------------------"

class DefineClass2:
    #__init__相当于python的构造函数，当实例化一个类的时候，会自动调用该方法
    def __init__(self):
        self.x = 1
        self.y = 2

    def prt(self):
        print "hello world"

print DefineClass2().x
print "---------------------"

class DefineClass3:
    #定义了一个初始化需要传递参数的类
    def __init__(self,str):
        self.str = str

    def prt(self):
        print self.str

DefineClass3("hello world !").prt()