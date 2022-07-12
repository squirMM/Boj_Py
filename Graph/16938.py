import sys
input=sys.stdin.readline

n,l,r,x=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()

def comb(arr,n):
    result=[]
    if n>len(arr):
        return result
    if n==1:
        for i in arr: result.append([i])
    elif n>1:
        for i in range(len(arr)-n+1):
            for j in comb(arr[i+1:],n-1):
                result.append([arr[i]]+j)
    return result

cnt=0
for i in range(2,n+1):
    for com in comb(arr,i):
        if l<=sum(com)<=r and com[-1]-com[0]>=x:
            cnt+=1
        
print(cnt)
