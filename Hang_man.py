import pygame
from random import randint
Word_list = ["computer", "surfboard", "robot", "trophy", "printer", "globe", "moniter", "magnolia", "renovation"]
randomNum = randint(0, 8)
randomWord = Word_list[randomNum]
#print(Word_list[randomWord])
lettersAvalible = ["a", "b", "c", "d" ,"e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lettersUsed = []
j = 1
word = []
for j in range(len(randomWord)):
    word.append(" _ ")
tries = 10
playing = True

while playing:
    
    
    print("letters Avalible: " , lettersAvalible)
    print("Letters used: " , lettersUsed)
    print(" word so far: ")
    for k in range(len(word)):
        print(word[k], end=" ")

    print("")
    letterPlayed = str(input("please input your selected letter: "))
    i = 0
    for i in range(26):
        if letterPlayed == lettersAvalible[i]:
            lettersAvalible[i] = " "
    lettersUsed.append(letterPlayed)
    k = 0
    l = 0
    for l in range(len(randomWord)):
        if letterPlayed == randomWord[l]:
            word[l] = letterPlayed
        

    print("tries left: ", tries)

    tempword = ""
    r = 1
    for r in range(len(word)):
        tempword = tempword + word[r]
    

    if tempword == randomWord:
        playing = False
    else:
        tries -= 1
        print("tries left: " ,tries)
print("you win the word was: ", randomWord)
#test  