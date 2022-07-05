import sys
input=sys.stdin.readline

s=input().strip()

dic={}
for l in s:
    if l in dic:
        dic[l]+=1
    else:
        dic[l]=1
dic=sorted(dic.items())

center=""
ans=""
for l,c in dic:
    times=int(c/2)
    ans+=l*times
    if c%2==1:
        if len(center)==0:center+=l
        else:
            print("I'm Sorry Hansoo")
            break
else:
    print(ans+center+ans[::-1])
