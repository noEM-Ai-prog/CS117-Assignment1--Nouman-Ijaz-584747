# decimal to binary converter
def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary = ""
    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2
        
    return binary

num = int(input("Enter a positive decimal number: "))
result = decimal_to_binary(num)
print(f"Binary representation: {result}")