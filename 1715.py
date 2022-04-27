import sys
from heapq import *
input=sys.stdin.readline

n=int(input())
q=[]
# 배열로 만들고 heapfify 가능
for _ in range(n):
    heappush(q,int(input()))

def find_num():
    
    if n==1:
        return 0
    remember=0
    while len(q)>1:
        f=heappop(q)
        s=heappop(q)
        remember+=(f+s)
        heappush(q,f+s)
    return remember

print(find_num())
