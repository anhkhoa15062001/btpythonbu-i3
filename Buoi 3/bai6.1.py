import math
# TIM SO NGUYEN TO
def timsonguyento():
  N = int(input("Nhap 1 so bat ki: "))
  if N < 2:
    return False
  for i in range(2, int(math.sqrt(N))+1):
    if N % i == 0:
      return False
  return True
if timsonguyento():
  print("No la so nguyen to")
else:
  print("Khong phai la so nguyen to") 