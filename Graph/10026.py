import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
rgbMap=[list(input().strip())for _ in range(n)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def case_(case,color,newColor):
    if color==newColor:
        return True
    if case ==1:
        if color != "B" and newColor !="B":
            return True
    return False
        

def bfs(case,startY,startX):
    global start
    
    q=deque([(startY,startX)])
    visit[startY][startX]=True

    while q:
        y,x=q.popleft()

        # 인접한 좌표 
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i]
            if 0<=ny<n and 0<=nx<n and not visit[ny][nx]:
                if case_(case,rgbMap[y][x],rgbMap[ny][nx]):
                    q.append((ny,nx))
                    visit[ny][nx]=True
                else:
                    start.append((ny,nx))
                
ans=[0,0]
for case in range(2):
    start=[(0,0)]
    visit=[[False]*n for _ in range(n)]
    while start:
        y,x=start.pop()
        if not visit[y][x]:
            bfs(case,y,x)
            ans[case]+=1


print(*ans,sep=" ")
