#coding:utf-8

#没有参数的函数
def method1():
    print "hello world"

method1()
print "----------------------"

#该函数必须传递一个参数【必选参数】
def method2(arg):
    print arg

method2("hello")
print "----------------------"


#给出一个可选参数的函数，可传参数，可不传参数（类似于java中的方法发重载）【可选参数】
def method3(arg = ""):
    if arg == "":
        print "没有传递参数"
    else:
        print arg

method3()
method3("world")
print "----------------------"


#给出一个接受元组的参数
def method4(*arg):
    for i in arg:
        print i

method4("aaa","bbb","ccc","ddd")
print "----------------------"

#给出一个接受字典的参数
def method5(**arg):
    keys = arg.keys()
    for i in keys:
        print i + " : " + str(arg[i])

method5(name="lili",age=23,sex="man")