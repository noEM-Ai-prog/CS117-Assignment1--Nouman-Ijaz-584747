# star to delta formation
def star_to_delta(ra, rb, rc):
    r_numerator = (ra * rb) + (rb * rc) + (rc * ra)
    rab = round(r_numerator / rc, 2)
    rbc = round(r_numerator / ra, 2)
    rca = round(r_numerator / rb, 2)
    return rab, rbc, rca

ra = float(input("Enter resistance ra: "))
rb = float(input("Enter resistance rb: "))
rc = float(input("Enter resistance rc: "))

rab, rbc, rca = star_to_delta(ra, rb, rc)
print(f"Equivalent Delta resistances (Rab, Rbc, Rca): {rab}, {rbc}, {rca}")