import sys
input=sys.stdin.readline
from collections import Counter

n=int(input())
arr=list(input().strip() for _ in range(n))
dic=Counter(arr)
dic=sorted(dic.items(),key=lambda x:(-x[1],x[0]))

print(dic[0][0])
