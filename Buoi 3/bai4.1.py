import math
# TONG LE
def tongle():
  N= int(input("Nhap so le: "))
  x = 0
  while N % 2 ==0:
    N= int(input("Nhap lai: "))
  for i in range(N):
     i += 1
     if i % 2 != 0:
      x += i
  print(x)
tongle()