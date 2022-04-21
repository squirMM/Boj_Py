import sys
input=sys.stdin.readline

expression=input().strip()
remote=[]


pNum=0
tmp=""
for a in expression:
    if a=="+" or a=="-":
        pNum+=int(tmp)
        tmp=""
        if a=="-":
            remote.append(pNum)
            pNum=0
    # if number?
    else:
        tmp=tmp+a

remote.append(pNum+int(tmp))

if len(remote)==1:
    print(remote[0])
else:
    ans=remote[0]
    for i in range (1,len(remote)):
        ans-=remote[i]
    print(ans)

