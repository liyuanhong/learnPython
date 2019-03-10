#coding:utf-8

class cla1:
    cla1 = "dog"

class cla2:
    cla2 = "cat"

#python支持多重继承，同时继承了两个类
class cla3(cla1,cla2):
    cla3 = "house"

    def printCla(self):
        print self.cla1
        print self.cla2
        print self.cla3

cla = cla3()
cla.printCla()
print cla.cla2