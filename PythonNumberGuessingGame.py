#Python number guessing game

import random
surrender = "Y"
lowest_num = 1
highest_num = 100
number = random.randint(lowest_num, highest_num)
guess = 0

print("######################")
print(" NUMBER GUESSING GAME ")
print("######################")

while(surrender == "Y"):
    guess= int(input("Guess a number!: "))
    if guess == number:
        print("Congratulations, you guessed it!")
        break;
    elif(guess > number):
        print("Your guess is too high.")
        surrender = input("TYPE Y TO CONTINUE! ANY OTHER TO SURRENDER... ").upper()
    elif(guess < number):
        print("Your guess is too low.")
        surrender = input("TYPE Y TO CONTINUE! ANY OTHER TO SURRENDER... ").upper()
    if(surrender != "Y"):
        print("Thank you for playing, you are too weak!")
