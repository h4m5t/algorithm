def bubble_sort(li):
    for i in range(len(li)):     #第i趟
        for j in range(len(li)-i-1):

            #如果要降序排列，只需修改>为<
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]
import random

#生成包含50个元素的随机数组
list1=[random.randint(1,1000) for i in range(50)]

print(list1)
bubble_sort(list1)
print(list1)


