#选择排序
def find_smallest(arr):
    smallest=arr[0]
    index=0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            index=i

    #返回最小值的下标
    return index

def selection_sort(li):
    new_li=[]
    for i in range(len(li)):
        smallest=find_smallest(li)
        new_li.append(li.pop(smallest))
    return new_li

list1=[2,4,5,6,7,12,1,87]

print(selection_sort(list1))

    