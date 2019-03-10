#coding:utf-8
coin = 30000
for i in range(20):
    coin = coin + coin * 0.2

print str(int(coin)) + "元"

coin = 10000
for i in range(30):
    if(i < 10):
        coin = coin + coin * 0.1 + 10000
    else:
        coin = coin + coin * 0.1

print str(int(coin)) + "元"

coin = 10000
for i in range(30):
    if(i < 10):
        pass
    else:
        coin = coin + coin * 0.1 + 10000

print str(int(coin)) + "元"
