# resistor tolerance sorting
perc_1_bin_count = 0
perc_5_bin_count = 0
reject_bin_count = 0

x=1
while x < 2:
    y = float(input("Enter measured resistor value: "))
    if y >= 99.0 and y <= 101.0:
        perc_1_bin_count += 1
    elif y >= 95.0 and y <= 105.0:
        perc_5_bin_count += 1
    elif y == 0:
        print("The count for 1 percent tolerance bin is: ", perc_1_bin_count)
        print("The count for 5 percent tolerance bin is: ", perc_5_bin_count)
        print("The count for reject bin is: ", reject_bin_count)
        break
    else:
        reject_bin_count += 1