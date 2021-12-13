import random

Start = "y"

FirstRandomNumber = float(random.randint(0,9))
SecondRandomNumber = float(random.randint(0,9))
ThirdRandomNumber = float(random.randint(0,9))

def Lottery(Start):
    while Start == "y":
        FirstNumber = float(input("Enter your first number: "))
        SecondNumber = float(input("Enter your second number: "))
        ThirdNumber = float(input("Enter your third number: "))
        if FirstNumber == FirstRandomNumber and SecondNumber == SecondRandomNumber and ThirdNumber == ThirdRandomNumber:
            print("Winner")
            print(f"The winning numbers are {FirstRandomNumber}, {SecondRandomNumber}, and {ThirdRandomNumber}. ")
            Start = "n"
            Start = input("Would you like to try again? y/n: ")
            
        else:
            print(f"You lose.")
            print(f"Sayang lods, {FirstRandomNumber}, {SecondRandomNumber}, and {ThirdRandomNumber} yung tamang sagot")
            Start = "n"
            Start = input("Would you like to try again? y/n: ")
            
    if Start == "n":
        print("Thank you for playing!")

Lottery(Start)

 

