msg = input("Enter any message: ")
val_1 = "make a lot of money"
val_2 = "buy now"
val_3 = "subscribe this"
val_4 = "click this"
if((val_1 in msg) or (val_2 in msg) or (val_3 in msg) or (val_4 in msg)):
    print("spam")
else:
    print("not Spam")