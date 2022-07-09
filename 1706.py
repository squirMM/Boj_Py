import sys
input=sys.stdin.readline

r,c=map(int,input().split())
arr=[list(input().strip()) for _ in range (r)]

ans=[]
for i in range(r):
    ans.extend("".join(arr[i]).split("#"))

arr=list(zip(*arr))
for i in range(c):
    ans.extend("".join(arr[i]).split("#"))

#ans=list(filter(lambda x: len(x)>1, ans))
ans=[x for x in ans if len(x)>1]
ans.sort()
print(ans[0])
