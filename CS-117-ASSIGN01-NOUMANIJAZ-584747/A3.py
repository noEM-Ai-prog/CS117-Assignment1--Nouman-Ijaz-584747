# resistors color code
color_name = str(input("Enter the color: "))
lowered = color_name.lower()
if lowered == 'black':
    print("The value of this color is 0.  ")
elif lowered == 'brown':
    print("The value of this color is 1.  ")
elif lowered == 'red':
    print("The value of this color is 2.  ")
elif lowered == 'orange':
    print("The value of this color is 3.  ")
elif lowered == 'yellow':
    print("The value of this color is 4.  ")
elif lowered == 'green':
    print("The value of this color is 5.  ")
elif lowered == 'blue':
    print("The value of this color is 6.  ")
elif lowered == 'violet':
    print("The value of this color is 7.  ")
elif lowered == 'grey':
    print("The value of this color is 8.  ")
elif lowered == 'white':
    print("The value of this color is 9.  ")
else:
    print("Invalid color. ")
