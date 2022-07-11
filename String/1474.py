import sys
input=sys.stdin.readline

n,m=map(int, input().split())
s=[input().strip() for _ in range(n)]

m-=sum(map(len,s))

rem=m%(n-1)
num=m//(n-1)

ans=s[0]
for i in range (1,len(s)):
    if (ord("_")<ord(s[i][0])and rem>0) or rem==len(s)-i :
        ans+=("_"*(num+1)+s[i])
        rem-=1
    else:
        ans+=("_"*(num)+s[i])
print(ans)
