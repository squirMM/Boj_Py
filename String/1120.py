import sys
input=sys.stdin.readline

A,B=input().split()
lenA,lenB=len(A),len(B)

ans=float('INF')
for i in range(lenB-lenA+1):
    cnt=0
    for j in range(lenA):
        if A[j]!=B[i+j]:
            cnt+=1
    #ans=min(ans,cnt)
    if cnt<ans:
        ans=cnt

print(ans)
