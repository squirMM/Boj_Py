import sys
import heapq
input=sys.stdin.readline
INF=1e9

n,e=map(int,input().split())
graph=[[]for _ in range(n+1)]

for _ in range (e):
    a,b,c,=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

p1,p2=map(int,input().split())

def dijkstra(start,n):
    distance=[INF]*(n+1)
    q=[]
    distance[start]=0           
    heapq.heappush(q,(0,start))
    while q:
        cost,p=heapq.heappop(q)
        #이미 방문한 곳이라면?
        if distance[p]<cost:
            continue
        #다음 탐색
        for n in graph[p]:
            newCost=cost+n[1]
            if newCost<distance[n[0]]:
                distance[n[0]]=newCost
                heapq.heappush(q,(newCost,n[0]))
    return distance
            

original=dijkstra(1,n)
p1_distance=dijkstra(p1,n)
p2_distance=dijkstra(p2,n)

p1_path=original[p1]+p1_distance[p2]+p2_distance[n]
p2_path=original[p2]+p2_distance[p1]+p1_distance[n]

result=min(p1_path,p2_path)
print(result if result<INF else -1)
