import sys
input=sys.stdin.readline

n=int(input())
s=[input().strip() for _ in range(n)]

s.sort(key=lambda x : len(x))

arr=[]

for i in range(n):
    for j in range(i+1,n):
        if s[j].startswith(s[i]):
            break
    else:
        arr.append(s[i])

print(len(arr)if len(arr) !=0 else 1)
