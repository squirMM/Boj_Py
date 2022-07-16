import sys
input=sys.stdin.readline
import heapq

# 숫자로 변경 
def remote(s):
    if s=='0':
        return 0
    if s.isupper():
       return ord(s) - ord('A')+27
    else:
        return ord(s) - ord('a')+1

# mst 알고리즘
#합집합 연산
def union(x,y):
    px=find_parent(x)
    py=find_parent(y)

    if py!=px:
        if set_size[px]<set_size[py]:
            px,py=py,px
        make_set[py]=px
        if set_size[px]==set_size[py]:
            set_size[px]+=1
        return True
    return False
        

#분리집합 부모 찾
def find_parent(x):
    if x==make_set[x]:
        return x
    make_set[x]=find_parent(make_set[x])
    return make_set[x]

def kruskal(n,weight):
    heap=[]

    for i in range(n):
        for j in range(n):
            if i==j: continue
            if weight[i][j]>0:
                heapq.heappush(heap,(weight[i][j],i,j))
    cnt=1
    weight_sum=0
    while heap:
        w,v1,v2=heapq.heappop(heap)

        if union(v1,v2):
            weight_sum+=w
            cnt+=1
            
    return weight_sum if cnt==n else -1

if __name__ == "__main__":
    n=int(input())
    weight=[[0]*n for _ in range(n)]
    for i in range(n):
        tmp=input().strip()
        for j in range(n):
            weight[i][j]=remote(tmp[j])

    make_set=[i for i in range(n)]
    set_size=[1 for i in range(n)]

    w=kruskal(n,weight)
    if w==-1:
        print(-1)
    else:
        print(sum(map(sum,weight))-w)
