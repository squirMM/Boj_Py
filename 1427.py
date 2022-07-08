import sys
input=sys.stdin.readline

n=list(map(int,input().strip()))
n.sort(reverse=True)
print(*n,sep="")
