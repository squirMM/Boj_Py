import sys
input=sys.stdin.readline
from collections import deque

tc=int(input())
for _ in range(tc):
    com=input().strip()
    n=int(input())

    s=input().strip()
    arr=deque(s[1:-1].split(','))
    if n==0 : arr=[]

    #print(arr) 
    rev=0
    for c in com:
        if c=='R':
            rev+=1
        elif c=='D':
            if len(arr)==0:
                print("error")
                break
            else :
                if rev%2!=0:
                    arr.pop()
                else :
                    arr.popleft()
    else :
        if rev%2==0 :print("["+",".join(arr)+"]")
        else:
            arr.reverse()
            print("["+",".join(arr)+"]")
