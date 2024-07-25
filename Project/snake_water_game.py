import random

while (True):

    print("\n!! Enter 0 when you want to quit !!\n")

    cmp = random.choice(["w", "s", "g"])

    you = input(
        "!! Enter 's' for Snake, 'g' for Gun, 'w' for Water !!\n\n =>   ").lower()

    if (you == 0 or you == "0"):
        print("Thank you for playing! Goodbye!")
        break

    your_dict = {"w": "water",
                 "g": "gun",
                 "s": "snake"
                 }

    cmp_dict = {"w": "water",
                "g": "gun",
                "s": "snake"
                }

    def msg():
        print(f"You Choose: {your_dict[you].capitalize()}")
        print(f"Computer choose: {cmp_dict[cmp].capitalize()}")

    if (cmp == "w" and you == "g"):
        msg()
        print("You lose... but don't give up. Keep trying, and you'll get there!")
    elif (cmp == "w" and you == "s"):
        msg()
        print("You win! Your hard work and determination have paid off. Congratulations!")
    elif (cmp == "s" and you == "w"):
        msg()
        print("You lose... but don't give up. Keep trying, and you'll get there!")
    elif (cmp == "snake" and you == "g"):
        msg()
        print("You win! Your hard work and determination have paid off. Congratulations!")
    elif (cmp == "g" and you == "s"):
        msg()
        print("You lose... but don't give up. Keep trying, and you'll get there!")
    elif (cmp == "g" and you == "w"):
        msg()
        print("You win! Your hard work and determination have paid off. Congratulations!")
    elif (cmp == you):
        msg()
        print("The Game is Draw")
    else:
        print(
            f"!! You Choose {you}, which is wrong. Please enter - 's' or 'g' or 'w' !!")