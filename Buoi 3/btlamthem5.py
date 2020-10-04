import math
print("Dem chu hoa va chu thuong")
def count_upper_lower(str):
    upper=lower=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print(f"So chu hoa: {upper}|So chu thuong: {lower}")
str=input("Nhap chuoi: ")
count_upper_lower(str)