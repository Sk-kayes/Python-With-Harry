# The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random


def game():
    score = random.randint(1, 100)
    print(f"Your Score is: {score}")
    with open("Hi-score.txt", "r") as f:

        high_score = f.read()

        if (high_score != ""):
            high_score = int(high_score)
        else:
            high_score = 0

        print(f"High Score was: {high_score}")

        if (score > high_score):
            with open("Hi-score.txt", "w") as f:
                f.write(str(score))
            print(f"High Score updated to: {score}")

    return score


game()