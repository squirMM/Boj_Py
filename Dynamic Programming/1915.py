import sys
input=sys.stdin.readline

n,m=map(int,input().split())
dp=[[0]*m for _ in range (n)]

arr=[]
for i in range(n):
    arr.append(list(map(int,input().strip())))

    for j in range(m):
        if arr[i][j]==1:
            dp[i][j]=1


for i in range (1,n):
    for j in range(1,m):
        if arr[i][j]==0:continue
        if arr[i-1][j-1]==arr[i-1][j]==arr[i][j-1]==1:
            #최대 정사각형 만들 수 있는 경우 
            if dp[i-1][j-1]==dp[i-1][j]==dp[i][j-1]:
                dp[i][j]=dp[i-1][j-1]+1
            #이전에 0인 부분이 있어서 만들 수 없는 경우 
            else:
                dp[i][j]=min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        

ans=0
for a in dp:
    ans=max(ans,max(a))
print(ans**2)          
