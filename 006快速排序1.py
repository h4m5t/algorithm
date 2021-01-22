'''
Author: h4m5t
Date: 2021-01-18 20:17:29
LastEditTime: 2021-01-19 17:33:34
'''
def quicksort(li):
    if len(li)<2:
        return li
    else:
        #找一个基准值;取列表第一个元素
        mid=li[0]
        left_li=[i for i in li[1:] if i<=mid]
        right_li=[i for i in li[1:] if i>mid]
        
        li=quicksort(left_li)+[mid]+quicksort(right_li)
        return li
        #return quicksort(left_li)+[mid]+quicksort(right_li)
        

#test
import random
test_li=list(random.randint(1,100) for i in range(10))
print(test_li)

# a=quicksort(test_li)
# print(a)
# quicksort(test_li)
# print(test_li)


test_li1=list(range(1000))
random.shuffle(test_li1)
print(test_li1)
print(quicksort(test_li1))
