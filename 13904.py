import sys
import heapq
input=sys.stdin.readline

n=int(input())
max_d=0
q=[]
for _ in range(n):
    a,b=map(int,input().split())
    max_d=max(max_d,a)
    heapq.heappush(q,(-b,a))


def greedy():
    arr=[0]*max_d
    while q:
        w,d=heapq.heappop(q)
        for i in range(d-1,-1,-1):
            if arr[i]==0:
                arr[i]=-w
                break
    return (sum(arr))


print(greedy())
