import sys
input=sys.stdin.readline

n=int(input())
x,num,ans=[0]*26,9,0
for _ in range(n):
    s=input().strip()
    for i in range (len(s)):
        x[ord(s[i])-ord('A')]+=(10**(len(s)-i-1))

x.sort(reverse=True)

for a in x:
    ans,num=ans+a*num,num-1

print(ans)
    
