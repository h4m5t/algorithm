'''
Author: h4m5t
Date: 2021-01-19 14:58:38
LastEditTime: 2021-01-19 15:29:23
'''
'''
堆排序的过程
1.建立堆
2.得到堆顶元素，即最大元素
3.去掉堆顶，将堆最后一个元素放到堆顶，通过一次向下调整使堆有序
4.堆顶元素为第二大元素
5.重复步骤3，直到堆空
'''
#此处用数组实现二叉树
#调整函数
def sift(li,low,high):
    """
    low:代表顶点
    high:代表最后一个元素
    """
    i=low
    j=i*2+1 #j为左孩子节点
    tmp=li[low] #堆顶元素
    while j<=high:
        if  j+1<=high and li[j+1]>li[j]:  #有右孩子且比较大
            j=j+1       #指向右孩子
        
        if li[j]>tmp:
            li[i]=li[j]
            i=j         #向下看一层
            j=i*2+1           
        else:
            li[i]=tmp      #放到中间层
            break
    else:                 #放到最下层
        li[i]=tmp

def heap_sort(li):
    n=len(li)
    #从最后一个非叶子节点建立堆
    for i in range((n-2)//2,-1,-1):
        #放缩方法，其中n-1表示整个堆的最后一个元素
        sift(li,i,n-1)
    
    for i in range(n-1,-1,-1):
        li[0],li[i]=li[i],li[0]
        sift(li,0,i-1)

test_li=[i for i in range(100)]
import random
random.shuffle(test_li)
print(test_li)
heap_sort(test_li)
print(test_li)




