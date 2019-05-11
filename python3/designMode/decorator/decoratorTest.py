#coding:utf-8

#############################################
#              装饰器测试
#############################################

from python3.designMode.decorator import myDecorator

#原始写法，使用装饰模式
def test1():
    print("this is test1")
myDecorator.debug1(test1)()

#通过@来使用装饰模式，更加
@myDecorator.debug2
def test2():
    print("this is test2")

test2()