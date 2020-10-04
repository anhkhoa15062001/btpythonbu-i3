import math
# TONG CHAN
def tongchan():
  N= int(input("Nhap so chan: "))
  x = 0
  while N % 2 !=0:
    N = int(input("Nhap lai: "))
  for i in range(N):
     if i % 2 == 0:
      x += i
  print(x)
tongchan()