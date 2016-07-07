'''Generate a random number from 1 to 10 (Look up the appropriate python class/function to do this)
Ask the user to guess the number.
Give the user three guess to get the number correct.
If the user guesses correctly, exit the game and congratulate the user.
If the user fails give the appropriate error message and exit the game.

If the user is within one of the correct answer display “Hot”
If the user is within two of the correct answer display “Warm”
All other guesses should display “Cold”
Upload the program to GitHub.'''

from random import randint
target = randint (1,11)
c = False

for a in range (0,3):
    guess = int(input("Guess a number from 1-10: "))

    if guess == target:
        print ("Congratulations, you guessed correctly!")
        c = True
        break

    elif target -1<=guess<=+1:
        print("Hot like a tamale")
    elif target -2<=guess<+2
        print("Warm like a summer breeze")
    else:
        print("Cold as ice")

if c == False
    print ("Three strikes, you\'re out.")