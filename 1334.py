import sys
input=sys.stdin.readline

s=input().strip()
n=len(s)
    
ans=s[:n//2]
if n%2==1:
    if ans+s[n//2]+ans[::-1]>s:
        ans=ans+s[n//2]+ans[::-1]
    else:
        tmp=str(int(ans+s[n//2])+1)
        if len(tmp)==len(ans)+2: ans=tmp[:-1]+tmp[:-1][::-1]
        else: ans=tmp+tmp[:-1][::-1]
        
if n%2==0:
    if ans+ans[::-1]>s:
        ans=ans+ans[::-1]
    else:
        tmp=str(int(s[:n//2])+1)
        if len(tmp)==len(ans)+1:ans=tmp+tmp[:-1][::-1]
        else :ans=tmp+tmp[::-1]
        

print(ans)
