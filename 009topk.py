'''
Author: h4m5t
Date: 2021-01-19 15:01:27
LastEditTime: 2021-01-19 15:30:20
'''
from heapq import *
import  random 
data = list(range(10)) 
random.shuffle(data)

print(data)
a=heapq.heappop()
print(a)

