def insert_sort(li):
    for i in range(1,len(li)):   #i表示摸到的牌
        j=i-1     #j表示手中已排好序的牌
        tmp=li[i]
        while tmp<li[j] and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=tmp
    return li

#test
import random
test_li=list(random.randint(1,100) for i in range(30))
print(test_li)

insert_sort(test_li)
print(test_li)

