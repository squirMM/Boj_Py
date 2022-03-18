str1=input()
str2=input()

#setting
str1="0"+str1
str2="0"+str2

n=len(str1)
m=len(str2)

#setting dp
#lcs[rows][cols]
lcs=[[0]*(m) for _ in range(n)]

#calculation lcs number
ansN=0
for i in range(0,n):
    for j in range (0,m):
        if i==0 or j==0:
            continue
        if str1[i]==str2[j]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i][j-1],lcs[i-1][j])

ansN=lcs[n-1][m-1]
print(ansN)

#calculation lcs
ansS=""
for_j=m-1

for i in range (n-1,0,-1):
    for j in range (for_j,0,-1):
        if str1[i]==str2[j] and lcs[i][j]==ansN:
            ansN-=1
            ansS=str1[i]+ansS
            for_j=j
            break
print(ansS)
