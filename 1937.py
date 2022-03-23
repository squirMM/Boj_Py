import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

n=int(input())
map_p=[list(map(int,input().split()))for _ in range(n)]

visit=[[-1 for _ in range(n)]for __ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def dfs(y,x):
    if visit[y][x]!=-1:
        return visit[y][x]
    visit[y][x]=1
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<n and 0<=nx<n:
            if map_p[y][x]<map_p[ny][nx]:
                visit[y][x]=max(visit[y][x],dfs(ny,nx)+1)
    return visit[y][x]      
    
ans=1
for y in range (n):
    for x in range(n):
        if visit[y][x]==-1:
            ans=max(ans,dfs(y,x))
print(ans)
