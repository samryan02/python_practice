#testing
#testing2
import random

def prompts():
    strength = int(input("on a scale of 1 to 5 how stong would you like your password to be: "))
    use = input("what is the use of this pass word: ")
    username = input("what is your use name email for this(if none enter null): ")
    answers = {'strength': strength,'use': use, 'username': username}
    return answers
def strength_1():

    fristLevel = ["password", "1234567", "picture", "ocean", "mansion", "arduino", "titanic"]
    listVar = random.randint(0,6)
    return fristLevel[listVar]
def strength_2():
    secondLevel = ["DoorFrame", "GrandPiano", "LargeTelevision", "OldXbox", "WishfullLlama", "AridSnail", "BigShip", "TallStaircase", "FancyDesk"]
    listVar = random.randint(0,8)
    return secondLevel[listVar]
def strength_3():
    TheirdLevel = ["DoorFrame", "GrandPiano", "LargeTelevision", "OldXbox", "WishfullLlama", "AridSnail", "BigShip", "TallStaircase", "FancyDesk"]
    listVar = random.randint(0,8)
    addon = str(random.randint(0,120))
    password = TheirdLevel[listVar] + addon
    return password
def strength_4():
    forthLevel = ["BigStickDiplomacy", "TheOnlyThingToFearIsFearItsSelf", "LiveFreeOrDie", "VictoryAtAllCosts", "WeShallDefendOurIsland", "GovermentOfThePeople", "WhatEverYouAreBeAGoodOne", "IntellectualsSolveProblemsGenuisesPerventThem","InformationIsNotKnowlage", "LoveIsABetterTeacherThanDuty, ", "TheFsterYouGoTheShorterYouAre"]
    listVar = random.randint(0,10)
    addon = str(random.randint(0,999))
    password = forthLevel[listVar] + addon
    return password
def strength_5():
    fithLevel = ["BigStickDiplomacy", "TheOnlyThingToFearIsFearItsSelf", "LiveFreeOrDie", "VictoryAtAllCosts", "WeShallDefendOurIsland", "GovermentOfThePeople", "WhatEverYouAreBeAGoodOne", "IntellectualsSolveProblemsGenuisesPerventThem","InformationIsNotKnowlage", "LoveIsABetterTeacherThanDuty, ", "TheFsterYouGoTheShorterYouAre"]
    listVar = random.randint(0,10)
    addon1 = str(random.randint(0,999))
    addon2 = chr(random.randint(35,38))
    addon3  =chr(random.randint(35,38))
    addon4 = chr(random.randint(35,38))
    password = fithLevel[listVar] + addon1 + addon2 + addon3 + addon4
    return password

def passowrdSelector(answers):
    if answers['strength'] == 1:
        password = strength_1()
        return password

    if answers['strength'] == 2:
        password = strength_2()
        return password

        
    if answers['strength'] == 3:
        password = strength_3()
        return password


    if answers['strength'] == 4:
        password = strength_4()
        return password


    if answers['strength'] == 5:
        password = strength_5()
        return password

def writeTofile(answers, passowrd):
    file1 = open("MyFile.txt","a+")
    fisrtline = "\n\n Use of password: " + answers['use']
    file1.write(fisrtline)
    secondline = "\n Username: " + answers['username']
    file1.write(secondline)
    theirdline = "\n password: " + passowrd
    file1.write(theirdline)
 
    file1.close() 


answers = prompts()


passowrd = passowrdSelector(answers)

writeTofile(answers, passowrd)


    



    