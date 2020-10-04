import math
# TINH TONG 
def tinhtong():
  N= int(input("nhap N: "))
  x = 0
  for i in range(1, N):
    i+=1
    x += pow(i,3)
  print(x)
tinhtong()