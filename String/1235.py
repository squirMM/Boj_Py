import sys
input=sys.stdin.readline

n=int(input())
arr=[ input().strip() for _ in range(n)]

k=-1
while True:
    tmp=[]
    for i in range(n):
        if i==0: tmp.append(arr[i][k:])
        else:
            if arr[i][k:]in tmp:
                break
            else:
                tmp.append(arr[i][k:])
    else:
        print(-k)
        break
    k-=1
