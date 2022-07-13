import sys
input=sys.stdin.readline
from collections import deque

dy=[0,0,1,-1]
dx=[1,-1,0,0]

dd=[(0,1),(1,0),(2,3),(3,2)]

ans=1e9
def bfs(r,c,dis):
    global ans
    visit=[[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)]
    visit[r-1][c-1][dis-1]=1

    q=deque()
    q.append([r-1,c-1,dis-1,0])

    while q:
        y,x,d,cnt =q.popleft()
        #도착한 경우 
        if y==end[0]-1 and x==end[1]-1 and d==end[2]-1:
            ans=min(ans,cnt)

        #방향 전환 x
        ny,nx=y,x
        for i in range(3):
            ny,nx=ny+dy[d],nx+dx[d]
            #print(y,x,ny,nx)
            if 0<=ny<m and 0<=nx<n:
                if visit[ny][nx][d]==1: continue
                if arr[ny][nx]==0 :
                    visit[ny][nx][d]=1
                    q.append([ny,nx,d,cnt+1])
                else: break
      
        #방향 전환
        for i in range(4):
            if d!=i and visit[y][x][i]==0:
                visit[y][x][i]=1
                if (d,i) in dd:
                    q.append([y,x,i,cnt+2])
                else:
                    q.append([y,x,i,cnt+1])
        

m,n=map(int,input().split())
arr=[list(map(int, input().split())) for _ in range (m)]

r,c,dis=map(int,input().split())
end=list(map(int,input().split()))
bfs(r,c,dis)
print(ans)
