import sys
input=sys.stdin.readline

n,m=map(int, input().split())
arr=[int(input())for _ in range(m)]

dp=[10000 for _ in range (n+1)]
dp_x=[0 for _ in range (n+1)]
dx=[-1,0,1]

dp[2],dp_x[2]=1,1
for i in range(2,n+1):
    for j in range(3):
        #몇 칸 뛸거야?
        nx=dp_x[i]+dx[j]
        if nx>0 and (i+nx) not in arr and (i+nx)<=n:
            if dp[i+nx]>dp[i]+1:
                dp[i+nx]=dp[i]+1
                dp_x[i+nx]=nx

if dp[n]==10000 or 2 in arr:
    print(-1)
else: print(dp[n])

print(dp)
print(dp_x)
