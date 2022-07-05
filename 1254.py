import sys
input=sys.stdin.readline

s=input().strip()

if s==s[::-1]:
    print(len(s))
else:
    ln=len(s)+1
    for i in range(1,len(s)):
        mid=int(ln/2)
        if ln%2==1 :
            #mid 제외 
            if s[:mid][::-1]==s[mid+1:]+s[:i][::-1]:
                print(ln)
                break
            else:
                ln+=1
        else:
            if s[:mid][::-1]==s[mid:]+s[i:][::-1]:
                print(ln)
                break
            else:
                ln+=1'
        
    else:
        print(2*len(s)-1)

        
