import sys
input=sys.stdin.readline

r,c=map(int,input().split())
load=[ list(input().strip()) for _ in range(r)]
visit=[[False]*(c) for _ in range(r)]
dy=[-1,0,1]


def check(y,x):
    if 0<=y<r and 0<=x<c:
        return True
    else:
        return False

ans=0
def dfs(y,x): 
    global ans
    # 끝까지 연결 했을 때 
    if x==c-1:
        ans+=1
        return True
    
    for i in range(len(dy)):
        ny,nx=y+dy[i],x+1
        if check(ny,nx) is False : continue
        if load[ny][nx]=='x'or visit[ny][nx]: continue
        visit[ny][nx]=True
        # 제어 장치 / 맨 끝까지 도달했다면 return으로 정지 
        if dfs(ny,nx): return True

for i in range(r):
    visit[i][0]=visit
    dfs(i,0)

print(ans)














