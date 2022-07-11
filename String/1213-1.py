import sys
from itertools import permutations
input=sys.stdin.readline

s=input().strip()
arr=list(set(permutations(s)))
arr.sort()

for i in arr:
    tmp="".join(i)
    if tmp==tmp[::-1]:
        print(tmp)
        break
else:
    print("I'm Sorry Hansoo")
