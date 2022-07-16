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
# 분리집합 클래스 
class DisjointSet:
    def __init__(self):
        self.parent=None

#합집합 연산
def unionset(set1,set2):
    set2=findset(set2)
    set2.parent=set1

#분리집합 부모 찾
def findset(s):
    while s.parent != None:
        s = s.parent

    return s

def kruskal(n,weight):
    vertex_set=[DisjointSet() for _ in range(n)] # 부분 집합
    heap=[]

    for i in range(n):
        for j in range(n):
            if i==j:continue
            if weight[i][j]>0:
                heapq.heappush(heap,(weight[i][j],i,j))
    cnt=1
    weight_sum=0
    while heap:
        w,v1,v2=heapq.heappop(heap)
        set1=vertex_set[v1] #집합
        set2=vertex_set[v2] #집합 

        if findset(set1)!=findset(set2):
            unionset(set1,set2) # 합집합 해줌 
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
    
    w=kruskal(n,weight)
    if w==-1:
        print(-1)
    else:
        print(sum(map(sum,weight))-w)
