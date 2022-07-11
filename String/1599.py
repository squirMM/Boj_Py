import sys
input=sys.stdin.readline

n=int(input())
arr=list(input().strip() for _ in range(n))

newR=list(map(str, 'a b k d e g h i l m n ng o p r s t u w y'.split()))

normal={}
for i in range(len(newR)):
    normal[newR[i]]=chr(97+i)

dic={}
for i in arr:
    new=''
    for j in range(len(i)):
        if i[j]=='n'and j+1<len(i) and i[j+1]=='g': new+=normal['ng']
        else:new+=normal[i[j]]
    
    dic[new]=i

print( *[dic[s] for s in sorted(dic)],sep="\n")

