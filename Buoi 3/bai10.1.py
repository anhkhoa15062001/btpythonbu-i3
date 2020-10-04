import math
# Tinh so fibonacci thu n
def fibo(n):
    "Ham tinh so fibonacci"
    if n==1 or n==2:
        return 1
    return fibo(n-1) + fibo(n-2)
print("nhap n:",end="")
n=int(input())
print(f"So fibo thu {n}: {fibo(n)}")
