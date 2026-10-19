# current direction
current = float(input(f"Enter the value of current: "))
if current > 0:
    print("The cuurent flows from A to B. ")
elif current < 0:
    print("The cuurent flows from B to A. ")
else:
    print("No current flows. ")