
for i in range(1, 6):
    for j in range(1, 5 - i + 1):
        print(" ", end="")
    for k in range(1, 2*i):
        print("*", end="")
    print()


row = int(input("write the amount of rows you want:"))
for i in range(1, row + 1):
    print(" " * (row - i), end="")
    print('*' * (2 * i - 1), end="")
    print()