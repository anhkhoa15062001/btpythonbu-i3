import math
print("max min")
def max_min(*numbers):
    print(f"Day so duoc truyen vao: {numbers}")
    return max(numbers),min(numbers)
max,min=max_min(1,3,15,10,2,50,100)
print(f"max: {max}, min: {min}")