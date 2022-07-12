import sys
import heapq
input=sys.stdin.readline
INF=1e9

n,m,x=map(int,input().split())
graph=[[] for _ in range(n+1) ]
for _ in range (m):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start,n):
    distance=[INF]*(n+1)
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        time,p=heapq.heappop(q)
        if distance[p]<time:
            continue
        for i in graph[p]:
            acTime=time+i[1]
            if acTime<distance[i[0]]:
                distance[i[0]]=acTime
                heapq.heappush(q,(acTime,i[0]))
    return distance
    
result=0
#집에 가는
comebackhome=dijkstra(x,n)
for i in range (1,n+1):
    gotoparty=dijkstra(i,n)
    result=max(result,gotoparty[x]+comebackhome[i])

print(result)
