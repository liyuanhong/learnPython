#coding:utf-8
'''
参考地址：https://docs.python.org/2/library/urllib2.html
'''
import urllib2


#发送一个get请求(默认发送的是GEt请求)
url = 'http://www.baidu.com'
result = urllib2.urlopen(url)
html = result.read()
print html

#发送一个POST请求（当添加了data参数的时候，就会使用POST请求）
url = 'http://www.baidu.com'
result = urllib2.urlopen(url,data="name=hong")
html = result.read()
print html


#添加header参数
url = 'http://www.baidu.com'
header = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}
res = urllib2.Request(url,headers=header)
result = urllib2.urlopen(res)
html = result.read()
print html