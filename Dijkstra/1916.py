import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)

n=int(input())
m=int(input())

#벡터처럼 구현 
graph=[[]for _ in range(n+1)]

#start부터 index까지의 최소값
distance=[INF]*(n+1)

for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

start,end=map(int,input().split())

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:      
        dist,now=heapq.heappop(q)
        #이미 최소값이라면?
        if distance[now]<dist:
            continue
        #(cost,도착지)
        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
        

dijkstra(start)
print(distance[end])

