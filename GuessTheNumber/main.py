import random

PLAY = input("Hello would you like to play the number guessing game? (y/n): ")

if PLAY == "y":
    print("The game is loading..")

elif PLAY == "n":
    print("Sorry to see you go!")
    quit()

else:
    print("What are you typing")
    quit()

num = random.randint(1, 101)

while True:
    guess = int(input("You are guessing numbers between 1-100 why don't you take a guess?: "))
    
    if guess == num:
        print("Well done you guess correctly")
        quit()
    else:
        print("Sorry you guessed incorrectly please try again!")