import sys
input=sys.stdin.readline

n=int(input())
s=[list(input().strip().split()) for _ in range(n)]

dic=set()
for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j][0].upper() not in dic:
            dic.add(s[i][j][0].upper())
            s[i][j]="["+s[i][j][0]+"]"+s[i][j][1:]
            break
    else:
        flag=False
        for j in range(len(s[i])):
            if flag: break
            for k in range(len(s[i][j])):
                if s[i][j][k].upper() not in dic:
                    dic.add(s[i][j][k].upper())
                    s[i][j]=s[i][j][:k]+"["+s[i][j][k]+"]"+s[i][j][k+1:]
                    flag=True
                    break

    
for i in range(len(s)):
    print(" ".join(s[i]))
