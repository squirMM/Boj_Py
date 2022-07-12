import sys
from collections import deque
input=sys.stdin.readline

r,c=map(int,input().split())
roadMap=[list(input().strip())for _ in range (r)]

y,x=map(int,input().split())
y,x=y-1,x-1
command=list(input().strip())

ans=[['#']*c for _ in range(r)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]

def bfs(starty,startx):
    global ans
    q=deque([(starty,startx)])
    alpha=roadMap[starty][startx]
    while q:
        y,x=q.popleft()
        for i in range(4):
            ny,nx=y+dy[i],x+dx[i] 
            if 0<=ny<r and 0<=nx<c and ans[ny][nx]=='#':
                if alpha==roadMap[ny][nx]:
                    q.append((ny,nx))
                    ans[ny][nx]='.'
        

def move(command,y,x):
    global ans
    dic={"U":0,"D":1,"L":2,"R":3}
    for com in command:
        if com=='W':
            ans[y][x]='.'
            bfs(y,x)
        else:
            y+=dy[dic[com]]
            x+=dx[dic[com]]

    ans[y][x]='.'
    for i in range(4):
        ny,nx=y+dy[i],x+dx[i]
        if 0<=ny<r and 0<=nx<c:
            ans[ny][nx]='.'
        

move(command,y,x)
        
for i in ans:
    print("".join(i))
