# loaded and unloaded voltage
def loaded_divider(vs, r1, r2, rl):
    unloaded_voltage = vs * (r2 / (r1 + r2))
    r_parallel = (r2 * rl) / (r2 + rl)
    loaded_voltage = vs * (r_parallel / (r1 + r_parallel))
    return unloaded_voltage, loaded_voltage

vs = float(input("Enter source voltage (vs): "))
r1 = float(input("Enter resistance r1: "))
r2 = float(input("Enter resistance r2: "))
rl = float(input("Enter load resistance (rl): "))

result = loaded_divider(vs, r1, r2, rl)
print(f"Unloaded and loaded voltages: {result}")