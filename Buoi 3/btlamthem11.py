import math
print("Tim day Fibonacci theo de quy")
def fibo_dequy(n):
    if n==1 or n==2:
        return 1
    return fibo_dequy(n-1) + fibo_dequy(n-2)
print("Tim Fibonacci khong theo de quy ")
def fibo_thuong(n):
    n1=0
    n2=1
    for i in range(n-1):
        temp=n1+n2
        n1=n2
        n2=temp
    return temp
print("nhap so fibo: ",end="")
n=int(input())
while n<=0:
    print("So khong hop le\n Nhap lai")
    print("nhap so fibo: ",end="")
    n=int(input())
print(f"De quy: {fibo_dequy(n)}")
print(f"Khong de quy: {fibo_thuong(n)}")