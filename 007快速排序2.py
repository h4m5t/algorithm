'''
Author: h4m5t
Date: 2021-01-19 14:58:10
LastEditTime: 2021-01-19 15:29:13
'''
#归位函数
def partition(li,left,right):
    tmp=li[left]
    #从右找一个，再从左找一个，向中间逼近
    while left<right:
        while left<right and li[right]>=tmp:
            right-=1
        li[left]=li[right]
        while left<right and li[left]<=tmp:
            left+=1
        li[right]=li[left]
    li[left]=tmp
    return left

def quick_sort(li,left,right):
    if left<right:
        mid=partition(li,left,right)
        quick_sort(li,left,mid-1)
        quick_sort(li,mid+1,right)

#test
list1=list(range(100))
import random
random.shuffle(list1)
print(list1)
quick_sort(list1,0,len(list1)-1)
print(list1)