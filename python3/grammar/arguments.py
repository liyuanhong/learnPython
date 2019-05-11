#coding:utf-8

#############################################
#              函数传参详解
#############################################

#一、传递普通参数
def test1(arg1):
    print(arg1)
print("-------------------------------")
test1("aaaaaaaaa")

#传递一个默认参数
def test2(arg1,arg2="bbb"):
    print(arg1)
    print(arg2)
print("-------------------------------")
test2("aaa")

#传递可变参数，加“*”时，函数可接受任意多个参数，全部放入一个元祖中
def test3(*arg1):
    print(arg1)
    for i in arg1:
        print(i)
print("-------------------------------")
test3("aaa",123,"333")

#传递可变参数，加“**”时，函数接受参数时，返回为字典
def test4(**arg1):
    keys = arg1.keys()
    for i in keys:
        print(arg1[i])
print("-------------------------------")
test4(a="aaahello",b=123,c= "333")

#混合的参数
def test5(*arg1,**arg2):
    print(arg1)
    print(arg2)

print("-------------------------------")
test5(1,2,3,4,5,a="aaahello",b=123,c= "333")

def test6(arg1,arg2="hello world",*arg3,**arg4):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)
    print("----------------->>>>>")

print("-------------------------------")
test6(100)
test6(100,1,2,3,4)
test6(100,"hello",1,2,3,4,a="aaa",b="bbb")
