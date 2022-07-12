import sys
input=sys.stdin.readline

n=int(input())
r=[int(input()) for _ in range(n)]

r.sort(reverse=True)

ans=0
for i in range(len(r)):
    ans=max(ans,r[i]*(i+1))
print(ans)
