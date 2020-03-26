import random

def randomNumGenerator(minimum, maximum):

    num = random.randint(minimum, maximum)
    return num

def checkIfCorrect(guess, correctNum):
    if guess == correctNum:
        return True
    else:
        return False

correctNum = randomNumGenerator(1, 10)
guesses = 0
while True:
    guesses = guesses +1
    guess = int(input("please input number: "))

    result = checkIfCorrect(guess, correctNum)

    if result == True:
        break


print("you guessed correctly in", guesses, "guesses")


