# parallel resistance
def parallel_resistance(resistors):
    reciprocal_sum = sum(1 / float(r) for r in resistors)
    return 1 / reciprocal_sum

n = int(input("Enter the number of resistors: "))
resistors = []

for i in range(n):
    val = float(input(f"Enter resistance for R{i+1}: "))
    resistors.append(val)

eq_resistance = parallel_resistance(resistors)
print(f"Equivalent resistance: {eq_resistance:.2f}")