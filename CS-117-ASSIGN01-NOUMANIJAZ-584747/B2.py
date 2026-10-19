#to ask user number of resistors and their values then printing their R equivalent in series
no_of_resistors = int(input("How many resistors are connected in series: "))
total_resistance = 0
for resistors in range (1, no_of_resistors + 1):
    values = int(input(f"Enter the value of resistor {resistors} (ohms): "))
    total_resistance = total_resistance + values
print("The total resistance is: ", total_resistance, "ohms")