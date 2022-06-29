import sys
input=sys.stdin.readline

s=input().strip()
bomb=input().strip()

n=len(bomb)
stack=[]
for c in s:
    stack.append(c)
    if c==bomb[-1] and "".join(stack[-n:])==bomb:
        del stack[-n:]

if stack:
    print("".join(stack))
else:print("FRULA")
