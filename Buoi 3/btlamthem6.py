import math
print("Chuoi pangram")
def is_pangram(str, alphabet):
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
str=input("Nhap chuoi muon kiem tra: ")
alphabet="abcdefghijklmnopqrstuvwxyz"
if is_pangram(str,alphabet):
    print(f" \"{str}\" True")
else:
    print(f" \"{str}\" False")
