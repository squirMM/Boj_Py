import sys
import heapq
input=sys.stdin.readline
INF=1e9

n=int(input())
m=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
mem=[-1]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        cost,p=heapq.heappop(q)
        if distance[p]<cost:
            continue
        for i in graph[p]:
            newCost=cost+i[1]
            if distance[i[0]]>newCost:
                distance[i[0]]=newCost
                heapq.heappush(q,(newCost,i[0]))
                mem[i[0]]=p

dijkstra(start)
ans=[]
p=end
while True:
    ans.append(p)
    if p==start: break
    p=mem[p]
print(distance[end])
print(len(ans))
for a in ans[::-1]:
    print(a,end=" ")
    

