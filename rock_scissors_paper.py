import random

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {ROCK : '🪨', SCISSOR : '✂️', PAPER : '📄'}
option = tuple(emojis.keys())

def get_player_choice():
    while True:
        player_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
        if player_choice in option:
            return player_choice
        else:
            print("Invalid choice!")

def display_choices(player_choice, computer_choice):
    print(f"You chose {emojis[player_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determining_winner(player_choice, computer_choice):
    if computer_choice == player_choice:
        print("Draw!")
    elif (
            computer_choice == ROCK and player_choice == PAPER  or
            computer_choice == PAPER  and player_choice == SCISSOR or
            computer_choice == SCISSOR and player_choice == ROCK):
        print("You win!")
    else:
        print("You lose!")

def play_game():
    while True:
        try:
            player_choice = get_player_choice()

            computer_choice = random.choice(option)

            display_choices(player_choice, computer_choice)

            determining_winner(player_choice, computer_choice)


            play_again = input("Continue Playing? (y/n): ").lower()
            if play_again == "n":
                print("Thank you for playing!")
                exit()

        except ValueError:
            print ("Invalid choice!")

play_game()