import math
print("So hoan hao")
def is_perfect(n):
    if(n<=0):
        return False
    if sum(i for i in range(1, n//2+1) if n%i==0)==n:
        return True
    else:
        return False
print("so muon kiem tra: ",end="")
n=int(input())
print(f"{n} True ") if is_perfect(n) else print(f"{n} False")
