import sys
input=sys.stdin.readline

tc,nw=map(int,input().split())
arr=[]
for _ in range(tc):
    a,b=map(int,input().split())
    arr.append((b,a))
arr.sort(key=lambda x : (x[0],-x[1]))

print(*arr,sep="\n")

ans=sys.maxsize
tw=arr[0][1]
times=1
flag=False
for i in range(1,len(arr)):

    #print(ans)
    if arr[i-1][0]== arr[i][0]:
        times+=1
    else:
        times=1
    tw+=arr[i][1]

    if tw>=nw:
        ans=min(ans,arr[i][0]*times)
        flag=True

print(ans if flag else -1)
    
    
        
    
