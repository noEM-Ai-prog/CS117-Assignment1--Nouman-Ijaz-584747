# sensor readings
readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count = 0
greatest_value = readings[0]
least_value = readings[0]
for i in readings:
    if i > greatest_value:
        greatest_value = i
print(f"The greatest value is: {greatest_value} ")
for j in readings:
    if j < least_value:
        least_value = j
print(f"The least value is: {least_value}")
for reading in readings:
    if reading > 3.2:
        count = count + 1
print(f"The number of values above 3.2 are: {count}")