#coding:utf-8
import  re

str = 'my name is honghong age 28 hellohello how are you hello hellohellohello hahahahah !'

#找到文中一个或多个连续的hello字符串
findStr = re.finditer(u'(hello)+',str)
for i in findStr:
    print i.group()
