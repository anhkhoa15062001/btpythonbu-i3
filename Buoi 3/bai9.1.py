import math
# bangcuuchuong
def bangcuuchuong(n):
    for i in range(1,11):
        print(f"{i}*{n}={i*n}")
print("nhap n: ",end="")
n=int(input())
bangcuuchuong(n)