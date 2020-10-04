import math
print("Kiem tra so nguyen to")
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True
print("Nhap so muon kiem tra: ",end="")
n=int(input())
if is_prime(n):
    print(f"{n} True")
else:
    print(f"{n} False")
