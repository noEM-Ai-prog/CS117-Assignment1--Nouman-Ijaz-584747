# smallest and largest resistor
resistors = []
for i in range(3):
    x = input(f"Enter the value of resistor {i+1}: ")
    resistors.append(x)

if resistors[0] > resistors[1] > resistors[2]:
    print(f"Largest = {resistors[0]} ohms")
elif resistors[0] < resistors[1] > resistors[2]:
    print(f"Largest = {resistors[1]} ohms")
elif resistors[0] < resistors[1] < resistors[2]:
    print(f"Largest = {resistors[2]} ohms")
if resistors[0] > resistors[1] > resistors[2]:
    print(f"Smallest = {resistors[2]} ohms")
elif resistors[0] < resistors[1] < resistors[2]:
    print(f"Smallest = {resistors[0]} ohms")
elif resistors[0] > resistors[1] < resistors[2]:
    print(f"Largest = {resistors[1]} ohms")

    