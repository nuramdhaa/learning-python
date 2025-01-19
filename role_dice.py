import random
import sys

while True:
    i = 1
    while True:
        play_count = str(i)
        print("Round: " + play_count)
        dice = input("Insert amount of dice: ")
        i += 1
        if int(dice) >= 1:
            print("Let us play")
            play = input("Roll the dice? (y/n): ").lower()
            if play == "y":
                result = [str((random.randint(1,6))) for _ in range (int(dice))]
                result_str = ", ".join(result)
                print(f"Rolled dice results: ({result_str})")
            elif play == "n":
                print("Thank you for playing.")
                break
            else:
                print("Error command. Please insert y or n.")
                ending = input("Keep playing? (y/n)").lower()
                if ending != "y":
                    print("Thank you for playing.")
                    sys.exit()
        else:
            print("Error number. Please Try again")
            ending = input ("Keep playing? (y/n)").lower()
            if ending != "y":
                print ("Thank you for playing.")
                sys.exit()