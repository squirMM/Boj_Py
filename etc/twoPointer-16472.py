import sys
input=sys.stdin.readline

def stoi(str):
    return int(ord(str)-97)

num=int(input())
arr=list(input().strip())

s,e,cnt,result=0,0,0,0
check=[0]*26

while(e<len(arr)):
    val=stoi(arr[e])
    if check[val]==0:cnt+=1
    check[val]+=1
    e+=1
    
    while (cnt>num):
        check[stoi(arr[s])]-=1
        if check[stoi(arr[s])]==0:
            cnt-=1
        s+=1
        
    result=max(result,e-s)

print(result)
