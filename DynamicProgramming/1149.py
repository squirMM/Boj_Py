import sys
input=sys.stdin.readline

#number of house
n=int(input())

#painting cost
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp=[[0]*3 for _ in range(n)]

def calCost():
    # number 1 house painting cost
    dp[0][0]=arr[0][0]
    dp[0][1]=arr[0][1]
    dp[0][2]=arr[0][2]

    for i in range(1,n):
        #choose R
        dp[i][0]=min(dp[i-1][1],dp[i-1][2])+arr[i][0]
        #choose G
        dp[i][1]=min(dp[i-1][0],dp[i-1][2])+arr[i][1]
        #choose B
        dp[i][2]=min(dp[i-1][0],dp[i-1][1])+arr[i][2]

    return min(dp[n-1])


print(calCost())

