#coding:utf-8

#############################################
#              定义好的装饰器
#############################################

def debug1(fun):
    def wrapper1():
        print("这是一个包装器wrapper1")
        return fun()
    return wrapper1

def debug2(fun):
    def wrapper2():
        print("这是一个包装器wrapper1")
        return fun()
    return wrapper2