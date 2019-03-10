#coding:utf-8

'''
使用正则表达group来分组截取字符串
'''

import re

'''
1. 正则表达式中的三组括号把匹配结果分成三组
 group() 同group（0）就是匹配正则表达式整体结果
 group(1) 列出第一个括号匹配部分，group(2) 列出第二个括号匹配部分，group(3) 列出第三个括号匹配部分。
2. 没有匹配成功的，re.search（）返回None
'''

#多行字符串
mulStr = '''
abc123ABC456aadoijlkaal;sd[,.adjfakajdlkjfel*6887
哈哈噢噢aa22Mffbb
hello world
'''

#单行字符串
str='abc123ABC'


result0 = re.search('([a-z]+)([0-9]+)([A-Z]+)',str).group(0)
result1 = re.search('([a-z]+)([0-9]+)([A-Z]+)',str).group(1)
result2 = re.search('([a-z]+)([0-9]+)([A-Z]+)',str).group(2)
result3 = re.search('([a-z]+)([0-9]+)([A-Z]+)',str).group(3)
print result0
print result1
print result2
print result3

parttern = re.compile('([a-z]+)([0-9]+)([A-Z]+)')
print parttern.findall(mulStr)