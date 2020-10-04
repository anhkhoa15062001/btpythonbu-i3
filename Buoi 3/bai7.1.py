import math
# TIM SO CHINH PHUONG
def sochinhphuong():
  N =  int(input("Nhap N: "))
  i =0
  while i * i <= N:
    if i * i == N:
      print("So nay la so chinh phuong")
      return 0
    i+=1
  print("So nay khong phai la so chinh phuong")  
sochinhphuong()