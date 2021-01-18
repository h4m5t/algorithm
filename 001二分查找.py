#二分查找
def binary_search(li,val):
    left=0
    right=len(li)-1

    #候选区有元素
    i=1
    while left<=right:
        
        print(f"查找第{i}次")
        i=i+1

        mid=(left+right)//2
        if li[mid]==val:
            return mid
        elif li[mid]>val:
            right=mid-1
        elif li[mid]<val:
            left=mid+1
    return None

#以下是测试
list1=range(50)

index=binary_search(list1,25)
print(index)
