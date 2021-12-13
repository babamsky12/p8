import random

RandomNumber = random.randint(0,100)
GuessNumber = int(input("Guess the random number between 0 to 100: "))

while GuessNumber != RandomNumber:
    if GuessNumber < RandomNumber:
        print("Less Than")
        print("Taasan mo pa lods")
        GuessNumber = int(input("Guess again: "))
    elif GuessNumber > RandomNumber:
        print("Greater Than")
        print("Ops, babaan mo onti")
        GuessNumber = int(input("Guesst again: "))

print("You guessed the random number!")