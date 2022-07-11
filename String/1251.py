import sys
input=sys.stdin.readline

s=input().strip()
n=len(s)

ans=[]
for i in range(1,n-1):
    for j in range(i+1,n):
        ans.append(s[:i][::-1]+s[i:j][::-1]+s[j:][::-1])
        print(i,j)

ans.sort()
print(ans[0])
