import sys
input=sys.stdin.readline

n=int(input())
arr=[list(input().strip()) for _ in range(n)]

onef=[]
for _ in range(n):
    onef.append([i for i,a in enumerate(arr[_]) if a=="Y"])

for i in onef:
    for a in range(len(i)-1):
        for b in range(a+1,len(i)):
            if arr[i[a]][i[b]]=="Y":continue
            arr[i[a]][i[b]]="Y"
            arr[i[b]][i[a]]="Y"

print(max([a.count("Y") for a in arr]))
