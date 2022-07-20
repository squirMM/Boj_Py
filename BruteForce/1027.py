import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))

ans=0
for i,v in enumerate(arr):
    tmp=0

    leftSlope=float('INF')
    rightSlope=-float('INF')

    # 왼 쪽
    for a in range(i-1,-1,-1):
        #기울기 
        slope =(v-arr[a])/(i-a)
        if slope<leftSlope:
            leftSlope=slope
            tmp+=1
    # 오른 쪽
    for b in range(i+1,n):
        #기울기 
        slope =(v-arr[b])/(i-b)
        if slope>rightSlope:
            rightSlope=slope
            tmp+=1

    ans=max(ans,tmp)

print(ans)
