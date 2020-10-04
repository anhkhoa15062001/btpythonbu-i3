import math

def dttron(r):
    s=math.pi*r*r
    return s
r=int(input("Nhap ban kinh: "))
print(f"Dien tich hinh tron co ban kinh {r}: {dttron(r)}")