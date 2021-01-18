#对数组进行递归求和
list1=list(range(1,101))
print(list1)

def li_sum(li):
    Sum=0
    #如果是空列表，停止
    if len(li)==0:
        return 0
    else:
        Sum=li[0]+li_sum(li[1:])
    
    return Sum
print(li_sum(list1))

#递归求数组长度
def lenth(li):
    if not li:
        return 0
    else:
        return 1+lenth(li[1:])

print(lenth(list1))



