import sys
input=sys.stdin.readline

n,m=map(int,input().split())
#map
arr=[['.']*m for _ in range (n)]

ic,ir=-1,-1
#rmap
rm=[]
for r in range(n):
    tmp=list(input().strip())
    if 'I' in tmp:
        ic=tmp.index('I')
        ir=r
    if 'R' in tmp:
        for c in range(m):
            if tmp[c]=='R':
                rm.append((r,c))

move=list(map(int,input().strip()))


def directionI(num):
    dx=[-1,0,1]
    dy=[1,0,-1]
    return (dy[num//3],dx[num%3])

def directionR(r,i):
    if i<r:
       return -1
    elif i==r:
        return 0
    else:
        return 1

def crash():
    count={}
    tmp=[]
    for i in rm:
        try:
            count[i]+=1
        except:
            count[i]=1
    for i,v in count.items():
        if v==1:tmp.append(i)
        
    return tmp

flag,icnt=True,0
for cnt in range(len(move)):
    ny,nx=directionI(move[cnt]-1)
    ir,ic=ir+ny,ic+nx
    icnt+=1
    if (ir,ic) in rm:
        print("kraj",icnt)
        flag=False
    j=0  
    while(flag):
        if j==len(rm):break
        rr,rc=rm[j]
        ny,nx=directionR(rr,ir),directionR(rc,ic)
        if rr+ny==ir and rc+nx==ic:
            print("kraj",icnt)
            flag=False
        rm[j]=(rr+ny,rc+nx)
        j+=1

    rm=crash()
    if flag==False: break
        
        
#성공시 출력    
if flag:
    arr[ir][ic]='I'
    for rr,rc in rm:
        arr[rr][rc]='R'   
    for a in arr:
        print("".join(a))
        
