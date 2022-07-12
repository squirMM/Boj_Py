import sys
import heapq
input=sys.stdin.readline

n,k=map(int,input().split())

jw=[]
for _ in range(n):
    #무게, 가격
    m,v=map(int,input().split())
    heapq.heappush(jw,(m,v))


bag=[]
for _ in range(k):
    w=int(input())
    heapq.heappush(bag,w)

def greedy():
    capable=[]
    ans=0
    
    for i in range(k):
        cap=heapq.heappop(bag)
        
        while jw and cap>=jw[0][0]:
            weight,money=heapq.heappop(jw)
            heapq.heappush(capable,-money)
        if capable:
            ans-=heapq.heappop(capable)
        elif not jw:
            break
    return ans
               
print(greedy())
