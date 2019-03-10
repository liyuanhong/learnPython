#coding:utf-8

'''
选择排序原理：
选择第一个数，依次和后面的数字比较，找到最小的那个数和第一个数交换
再从第二个数开始，依次和后面的数字比较，找到最小的那个数和第一个数交换
...
循环知道倒数第二个数和左右一个数比较完为止
到此排序完成
'''

data = [3,5,8,2,9,4,6,7]

def selectionSort(lyst):
    i = 0
    while i < len(lyst) - 1:
        minIndex = i;
        j = i + 1
        while j > len(lyst):
            if minIndex > j:
                minIndex = j
            temp = lyst[i]
            lyst[i] = lyst[j]
            lyst[j] = temp
            j = j + 1

        i = i + 1
    return lyst

print selectionSort(data)