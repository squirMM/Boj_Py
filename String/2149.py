import sys
input=sys.stdin.readline

key=input().strip()
s=input().strip()

row=len(s)//len(key)
arr=[]
for i in range(len(key)):
    arr.append(list(s[row*i:row*(i+1)]))

arr=list(zip(*arr))
arr.insert(0,list(sorted(key)))

ans=[]

arr_z=list(zip(*arr))
for i in key:
    ans.append(arr_z.pop(arr[0].index(i)))
    arr=list(zip(*arr_z))

ans=list(zip(*ans))
del ans[0]
print(*["".join(list(a)) for a in ans],sep="")
