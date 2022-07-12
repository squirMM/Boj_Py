import sys
input=sys.stdin.readline

def clockTurn(a,b):
    if b==1:
        return arr[a][7:]+arr[a][:7]
    else:
        return arr[a][1:]+arr[a][:1]

def turnLoop(a,b):
    #회전 로직
    arr[a]=clockTurn(a,b)
    side=b
    for i in range(a-1,-1,-1):
       if check[i]==1:
           side=-side
           arr[i]=clockTurn(i,side)
       else:
           break
    side=b
    for i in range(a+1,4):
        if check[i-1]==1:
            side=-side
            arr[i]=clockTurn(i,side)
        else:
            break
    return arr
        

# 입력
arr=[list(map(int,input().strip()))for _ in range(4)]
k=int(input())
check=[0 for _ in range(3)]

#몇바퀴?
for _ in range(k):
    for i in range(3):
        if arr[i][2]!=arr[i+1][6]:
            check[i]=1
        else:
            check[i]=0
    print(check)
    a,b=map(int,input().split())
    arr=turnLoop(a-1,b)
    for p in arr: print(p)
    print()
    
#합계
score={0:1,1:2,2:4,3:8}
ans=0
for i in range(4): 
    if arr[i][0]==1:
        ans+=score[i]
print(ans)



