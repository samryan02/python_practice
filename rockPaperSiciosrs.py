import random




while True:
    userSelection = input("please enter rock paper or scissors: ")
    if userSelection == "rock":
        print("paper")
    elif userSelection == "scissors":
        print("rock")
    elif userSelection == "paper":
        print("scissors")
    else:
        print("dont be stupid")