import sys
input=sys.stdin.readline

n,m=map(int,input().split())
home=[]
chicken=[]
for i in range(n):
    arr=list(map(int,input().split()))
    for j in range(n):
        if arr[j]==1:
            home.append([i,j])
        elif arr[j]==2:
            chicken.append([i,j])
            
dist=[list(map(lambda x : abs(x[0]-c[0]) + abs(x[1]-c[1]), home)) for c in chicken]

def comb(arr,n):
    result=[]
    if n==0:
        return [[]]
    elif n==len(arr):
        return [arr]
    for i in range(len(arr)):
        elem=arr[i]
        for rest in comb(arr[i+1:],n-1):
            result.append([elem]+rest)
    return result

answer=1e9
com=comb([i for i in range(len(chicken))],m)
for c in com:
    #tmp=zip(*[length[i] for i in c])
    res=sum(map(min,zip(*[dist[i] for i in c])))
        
    answer=min(answer,res) 

print(answer)
