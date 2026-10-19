# to print the current for values of voltage from 1 to 10 with a fixed resistance of 10 ohm
resistance = 10
for voltage in range (1, 11):
    print(f"V = {voltage} V, I = {voltage/resistance}")
