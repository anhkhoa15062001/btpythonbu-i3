import math
print("Ma tran")
def create_matrix(n,m):
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end="\t")
        print()
n=int(input("so hang la: "))
m=int(input("so cot la: "))
create_matrix(n,m)