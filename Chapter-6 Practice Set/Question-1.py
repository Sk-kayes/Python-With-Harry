num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))
num_4 = int(input("Enter fourth number: "))

if(num_1 > num_2):
    if(num_1 > num_3):
        if(num_1 > num_4):
            print(num_1)
        else:
            print(num_4)
    elif(num_3 > num_4):
        print(num_3)
    else:
        print(num_4)
elif(num_2 > num_3):
    if(num_2 > num_4):
        print(num_2)
    else:
        print(num_4)
elif(num_3 > num_4):
    print(num_3)
else:
    print(num_4)