import random

still_playing = "Y"
options = ("rock", "paper", "scissor")
machine_choice = random.choice(options)
human_choice = ""

while still_playing == "Y":
    human_choice = input("Rock, Paper, Scissor?: ").lower()
    if human_choice not in options:
        print("Sorry, that's not a valid option.")
        break
    elif human_choice == machine_choice:
        print("It's a tie!")
    elif human_choice == "rock" and machine_choice == "paper":
        print("I WIN, I CHOSE PAPER... YOU CHOSE ROCK!")
    elif human_choice == "paper" and machine_choice == "scissor":
        print("I WIN, I CHOSE SCISSOR... YOU CHOSE PAPER!")
    elif human_choice == "scissor" and machine_choice == "rock":
        print("I WIN, I CHOSE ROCK!")
    elif human_choice == "scissor" and machine_choice == "paper":
        print("YOU WIN, I CHOSE PAPER!")
    elif human_choice == "rock" and machine_choice == "scissor":
        print("YOU WIN, I CHOSE SCISSOR!")
    elif human_choice == "paper" and machine_choice == "rock":
        print("YOU WIN, I CHOSE PAPER!")
    still_playing = input("Do you want to play again? (Y/N): ").upper()
    machine_choice = random.choice(options)
