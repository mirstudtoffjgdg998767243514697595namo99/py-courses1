rows = 8579957
#int(input("Enter number of rows: "))
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))