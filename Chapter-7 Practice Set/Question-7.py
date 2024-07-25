row = int(input("Enter the row number: "))
for i in range(1, row+1):
    print(" "*(row-i), end=" ")
    print("*"*(2*i-1), end=" ")
    print("\n")