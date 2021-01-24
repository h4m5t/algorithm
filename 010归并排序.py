#(low,mid),(mid+1,high)
def merge(li,low,mid,high):
    i=low
    j=mid+1
    ltmp=[]
    while i<=mid and j<=high:
        if li[i]<li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
        j+=1
    li[low:high+1]=ltmp

#test
test_li=[1,3,5,7,2,4,6,8]
merge(test_li,0,3,7)
print(test_li)

