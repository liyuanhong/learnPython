#coding:utf-8
import yaml

#直接加载yaml格式的文本
data = yaml.load('''
-
  name: Mark McGwire
  hr:   65
  avg:  0.278
-
  name: Sammy Sosa
  hr:   63
  avg:  0.288es
''')
print(data)

#读取yaml文件并输出
stream = open('./file/test.yaml', 'r',encoding='utf-8')
str = stream.read()
print(yaml.load(str))

stream = open('./file/test1.yaml', 'r',encoding='utf-8')
str1 = stream.read()
print(yaml.load(str1))