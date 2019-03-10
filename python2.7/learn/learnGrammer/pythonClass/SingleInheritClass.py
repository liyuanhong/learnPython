#coding:utf-8

class People(object):
    className = "People"
    hair = "black"
    eyes = "black"
    mouth = "red"

    def __init__(self):
        print self.className
        pass

    def printInfo(self):
        print "hari : " + self.hair
        print "eyes :" + self.eyes
        print "mouth :" + self.mouth


class Man(People):
    sex = "man"
    className = "Man"

    def __init__(self):
        #调用父类构造方法
        super(Man,self).__init__()

    #第二种构造函数的写法
    # def __init__(self):
    #     People.__init___init__(self)

    def printInfo(self):
        super(Man,self).printInfo()
        print "sex : " + self.sex

man = Man()
man.printInfo()