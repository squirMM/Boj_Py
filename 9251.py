from sys import stdin

str1=stdin.readline().rstrip()
str2=input()

str1="0"+str1
str2="0"+str2

n=len(str1)
m=len(str2)

#make_dp
lcs=[[0]*(n) for _ in range(m)]

for i in range (0,m):
    for j in range(0,n):
        if i==0 or j==0 :
            continue;
        if str1[j]==str2[i]:
            lcs[i][j]=lcs[i-1][j-1]+1
        else:
            lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])

print(lcs[m-1][n-1])
