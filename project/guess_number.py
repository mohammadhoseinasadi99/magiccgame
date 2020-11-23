#Python project to guess a number that has randomly selected.
import random
number = random.randrange(0,100)
print("Welcome to Number Guess")
while True:

    response = int(input("enter a number between 0_100"))
    try:
        val = int(response)
    except ValueError :
        print("This is not a valid integer. Please try again")

    else:
        if val > number :
            print("This is higher than actual number. Please try again.")
        elif val < number:
            print("This is lower than actual number. Please try again.")
        else:
            print("This is the correct number")
    finally:
        print("Thank you for playing Number Guess. See you again")
