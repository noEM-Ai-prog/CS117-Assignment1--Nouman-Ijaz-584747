# logic gates
A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
if A and B == 1:
    print("AND = 1")
else:
    print("AND = 0")
if A or B == 1:
    print("OR = 1")
else:
    print("OR = 0")
if A == 1 and B == 0 or A==0 and B==1:
    print("XOR = 1")
else:
    print("XOR = 0")