import random
import sys

while True:
    number = random.randint (1, 100)
    while True:
        try:
            guess_number = int(input("Guess a random number from 1-100: "))
            if guess_number == number:
                print ("Congratulations! You guessed the right number.")
                play = input ("Continue playing? (y/n): ").lower()
                if play == "y":
                    break
                elif play =="n":
                    print("Thank you for playing.")
                    sys.exit()
                else:
                    print ("Please input y or n.")
            elif guess_number < number:
                print("Too low!")
            elif guess_number > number:
                print("Too high!")
            else:
                print("Please enter valid number.")
        except ValueError:
            print ("Please enter a valid number.")




