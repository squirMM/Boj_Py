import sys
input=sys.stdin.readline

tc=int(input())
numbers=[]

def check_numbers():
    ln=len(numbers)
    for idx in range(ln-1):
        nn=len(numbers[idx])
        if numbers[idx] == numbers[idx+1][:nn]:
            return False        
    return True

for _ in range(tc):
    n=int(input())
    numbers=list(input().strip() for __ in range(n))
    numbers.sort()
    if check_numbers():print("YES")
    else: print("NO")
        
        
