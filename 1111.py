import sys
input=sys.stdin.readline

n=int(input())
arr=list(map(int,input().split()))
    
if __name__=="__main__":
    if len(arr)==1:
        print('A')

    elif len(arr)==2:
        if arr[0]==arr[1]:
            print(arr[0])
        else:ㄴ
            print('A')
    else:
        if arr[1]==arr[0]:
            a=0
            b=arr[1]
        else:
            a=(arr[2]-arr[1])//(arr[1]-arr[0])
            b=arr[1]-arr[0]*a
            
        for i in range(1,n):
            if arr[i]!=arr[i-1]*a+b:
                print('B')
                break
        else:
            print(arr[n-1]*a+b)
            
