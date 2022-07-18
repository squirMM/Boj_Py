import sys
input=sys.stdin.readline
import math

def issquare(n):
    return True if int(n**0.5) == n**0.5 else False  

def isbound(x,y):
    if 0<=x<n and 0<=y<m:
        return True
    return False

n,m=map(int,input().split())
arr=[list(input().strip()) for _ in range(n)]

ans=-1
for x in range(n):
    for y in range(m):
        for dx in range(-n,n):
            for dy in range(-m,m):
                if dx==0 and dy==0: continue

                s=""
                cx,cy=x,y
                while isbound(cx,cy):
                    s+=arr[cx][cy]

                    if issquare(int(s)):
                        ans=max(ans,int(s))
                    cx+=dx
                    cy+=dy
print(ans)
