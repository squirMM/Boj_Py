import sys
input=sys.stdin.readline

s="0"+input().strip()
t="0"+input().strip()

ls=len(s)
lt=len(t)

dp=[[0]*ls for _ in range (lt)]

ans=0
for i in range (lt):
    for j in range(ls):
        if i==0 or j==0: continue
        if s[j]==t[i]:
            dp[i][j]=dp[i-1][j-1]+1
        #ans=max(ans,dp[i][j])

#for a in dp : print(a)
print(max(max(*dp)))
