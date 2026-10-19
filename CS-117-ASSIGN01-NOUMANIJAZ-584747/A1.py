# Fuse Check
voltage = float(input("Enter the value of voltage in volts: "))
resistance = float(input("Enter the value of resistance in ohms: "))
current = voltage/resistance
if resistance == 0 or resistance < 0:
    print("Invalid value of resistance. ")
else:
    print(f"The current is {current} A")
    if current <= 2:
        print("The circuit is safe. ")
    else:
        print("The fuse will blow.")
