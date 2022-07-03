import sys
import re
input=sys.stdin.readline

tc=int(input())
p=re.compile('(100+1+|01)+')
for _ in range(tc):
    s=input().strip()
    m=p.fullmatch(s)
    if m:print("YES")
    else:print("NO")
