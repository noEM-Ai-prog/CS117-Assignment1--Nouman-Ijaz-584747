# current and power
def ohms_current(v, r):
    return i
def power_dissipated(i, r):
    return p

v = float(input("Enter the value of voltage in volts: "))
r = float(input("Enter the value of resistance in ohms: "))

i = v/r
p = (i**2) * r

current = ohms_current(v, r)
power = power_dissipated(i, r)
print(f"Power dissipated = {power} W")
print(f"Current = {current} A")