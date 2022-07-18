import sys
input=sys.stdin.readline

n,k=map(int,input().split())

arr=[int(input())for i in range(n)]

dp=[0 for _ in range (k+1)]
dp[0]=1

def countNum():
    for i in arr:
       for j in range (i,k+1):
           if j>=i:
               dp[j]+=dp[j-i]

    return dp[k]

print(countNum())
