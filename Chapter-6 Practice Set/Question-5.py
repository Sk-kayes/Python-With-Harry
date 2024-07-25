list = ["sk", "kayes", "mousin", "nishat", "akhtar", "ansari"]
user_input = input("Enter name: ")
if(user_input in list):
    print(f"{user_input} is present in the list")
else:
    print(f"{user_input} is not present in the list")
