from random import randint, choice
from itertools import *


gamestarted = False
first = True
feedbackgiven = False
soclose = False

allnums = [1, 2, 3, 4, 5, 6]
choicelist = []
colorcode = []
notnum = []
allcombos = []
newcombos = []
usedcombos = []

print("welcome")

def welcome():
    #Just some giberish to lead the player into the game

    global gamestarted

    while not gamestarted:
        upforgame = str(input("are you up for a game? (yes/no) ")).lower()
        if upforgame == "yes":
            print("GREAT!")
            while upforgame == "yes":
                side = str(input("do you want to guess or make the code? (guess/code) ")).lower()
                if side == "guess":
                    print("good luck, and enjoy")
                    gamestarted = True
                    return (playerguess())
                elif side == "code":
                    print("good luck, and enjoy")
                    gamestarted = True

                    #might want to add some form of AI selection (simple/etc/etc)

                    return (playercode())

                elif side == "quit":
                    print("goodbye then")
                    return ("")
                else:
                    print("please answer with 'guess' or 'code', or type 'quit' to stop")
                    continue
        elif upforgame == "no":
            print("goodbye then")
            return ("")
        else:
            print("please answer with yes or no")
            continue



def playercode():
    codepicked = False
    colors = ["black", "white", "red", "green", "yellow", "blue"]
    global colorcode

#player creates the code -->
    while not codepicked:
        print("The possible colors for a code are: Red, Blue, Yellow, Green, Black and White")
        colorcode = ((str(input("Choose the colors of your code: "))).lower()).split(", ")

        #check if the right colors are used
        for i in range(len(colorcode)):
            if colorcode[i] in colors:
                continue
            else:
                print("please use a valid color")


        codepicked = True

    return AIturn(randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6))

def AIturn(Color1, Color2, Color3, Color4):


    global first
    global choicelist
    global allnums
    global colorcode
    global notnum

    print(first)

    while not first:
        if soclose == True: #if feedback was 4
            nextguess = [Color1, Color2, Color3, Color4]
        else: #if feedback wasn't 4
            nextguess = [Color1, Color2, Color3, Color4]
            print(f"now the AI guessed: {nextguess}")
            choicelist = choicelist.clear() #clearing the list so there won't be any duplicates affecting random chances
        return Playerturn(nextguess)
    while first: #first completely random guess
        firstguess = [Color1, Color2, Color3, Color4]
        first = False
        print(f"AI guessed: {firstguess}")
        return Playerfeedback(firstguess)

def Playerfeedback(code):

    global feedbackgiven
    global choicelist
    global allnums
    global soclose
    global notnum

    if code == colorcode: #doesn't work yet, cuz int != string
        return ("the AI wins")

    while not feedbackgiven: #makes sure you can't give feedback bigger >= 5
        goedgoed = int(input("Write down how many colors are in the right spot: "))
        goedfout = int(input("Write down how many colors are correct but not in the right spot: "))
        if goedgoed + goedfout <= 4:
            feedback = (goedgoed, goedfout)
            print(feedback)
            feedbackgiven = True
        else:
            print("please use numbers 1-4 where the total <= 4")


    if soclose == False: #if the feedbacks hasn't been 4 before
        for i in range(1):
            print(i)
            if goedgoed + goedfout == 4: #cuts the loop, making sure only the current colors can be chosen
                choicelist.append(code[i])
                choicelist.append(code[i+1])
                choicelist.append(code[i+2])
                choicelist.append(code[i+3])
                soclose = True
                return AIturn(choice(choicelist), choice(choicelist), choice(choicelist), choice(choicelist))

            elif feedback == (0,0): #throws away all numbers used in the code ##needs something extra to not let those numbers get back into the list
                choicelist = [item for item in allnums if item not in code]
                notnum = allnums - choicelist

            else:
                codecut = list(dict.fromkeys(code)) #removes duplicate numbers to create equal chances in the random
                """could be better"""
                if goedgoed + goedfout == 1:
                    choicelist.append(codecut[i])
                    feedbackgiven = False
                    return AIturn(randint(1,6), randint(1,6), randint(1,6), choice(choicelist))
                if goedgoed + goedfout == 2:
                    choicelist.append(codecut[i])
                    choicelist.append(codecut[i + 1])
                    feedbackgiven = False
                    return AIturn(randint(1, 6), randint(1,6), choice(choicelist), choice(choicelist))
                if goedgoed + goedfout == 3:
                    choicelist.append(codecut[i])
                    choicelist.append(codecut[i + 1])
                    choicelist.append(codecut[i + 2])
                    feedbackgiven = False
                    return AIturn(randint(1, 6), choice(choicelist), choice(choicelist), choice(choicelist))


    if soclose == True:
        return AIturn(choice(choicelist), choice(choicelist), choice(choicelist), choice(choicelist))





"""Systeem om alle keuzes in een lijst te hebben, en de volgende mogelijke combinaties toevoegen aan een nieuwe lijst"""

#nieuw hoogstwaarschijnlijk beter systeem
#def producttolist(): #could be used if stuff is used multiple times exactly the same

def Allcombos(): #creates a starting list of all possible combinations

    global allcombos

    allcombos = []
    tuples = []

    results = product("ABCDEF", repeat=4)
    for i in results:
        tuples.append(i)

    for i in tuples:
        j = "".join(i)
        allcombos.append(j)

    return AIguessing(allcombos)


def AIguessing(list):

    AIguess = choice(list)

    while not feedbackgiven: #makes sure you can't give feedback bigger >= 5
        correct = int(input("Write down how many colors are in the right spot: "))
        semicorrect = int(input("Write down how many colors are correct but not in the right spot: "))

        feedback = correct + semicorrect
        if feedback <= 4:
            return NewFeedbackSystem(AIguess, feedback)
        else:
            print("please use numbers 1-4 where the total <= 4")

def NewFeedbackSystem(guess, feedback):

    global allcombos
    global newcombos
    global usedcombos
    letters = ["A", "B", "C", "D", "E", "F"]
    tuples = []

    newcombos.clear()

    for i in range(1):
        Color1 = guess[i]
        Color2 = guess[i+1]
        Color3 = guess[i+2]
        Color4 = guess[i+3]

        if feedback == 4: #needs a fix
            #takes all letters in the code and checks for possible new combinations, adds them to the list
            results = permutations(f"{Color1}{Color2}{Color3}{Color4}", 4)
            for i in results:
                tuples.append(i)

            for i in tuples:
                j = "".join(i)
                newcombos.append(j)

            newcombos = [item for item in newcombos if item not in usedcombos]
            return newcombos

        elif feedback == 3:
            #takes all letters in the code and checks for possible new combinations with >= 3 from previous code, adds them to the list
            continue
        elif feedback == 2:
            #takes all letters in the code and checks for possible new combinations with >= 2 from previous code, adds them to the list
            continue
        elif feedback == 1:
            #takes all letters in the code and checks for possible new combinations with >= 1 from previous code, adds them to the list


            return AIguessing(newcombos)
        else:
            #takes all letters in the code and checks for possible new combinations WITHOUT these letters, adds them to the list
            newletterlist = [item for item in letters if item not in guess] #creates a new list with letters that weren't used
            newletters = "".join(newletterlist)
            print(newletters)

            results = product(newletters, repeat=4)
            for i in results:
                tuples.append(i)

            for i in tuples:
                j = "".join(i)
                newcombos.append(j)

            newcombos = [item for item in newcombos if item not in usedcombos]
            return newcombos

print(NewFeedbackSystem("ABCD", 4))
print(NewFeedbackSystem("AABB", 0))






def playerguess():
    turnsleft = 10
    PlayerTurn = True
    guessentered = False
    wit = 0
    zwart = 0

    colorlist = ["black", "white", "red", "green", "yellow", "blue"]
    previousguesses = {
        #guess : feedback
    }

    code = [choice(colorlist), choice(colorlist), choice(colorlist), choice(colorlist)]
    print(code)

    while PlayerTurn:
        print(previousguesses)
        while not guessentered:
            guess = ((str(input("Please type in a code (make sure to use a ', ' between each color): "))).lower()).split(", ")
            if len(guess) != 4:
                print("please use the correct format and choose 4 colors")
                continue
            else:
                guessentered = True
            print(guess)


        while guessentered:
            codeExtra = code

            for i in range(len(guess)):

                """The following code needs to be fixed
                    - when a color is entered multiple times but only exists once, they will still be counted and give false feedback
                """

                if guess[i] == code[i]: #kleur goed + goede plek
                    #if guess[i] in codeExtra:
                        wit += 1
                    #    codeExtra.remove(guess[i])
                elif guess[i] in code: #kleur goed + niet goede plek
                    #if guess[i] in codeExtra:
                        zwart += 1
                    #    codeExtra.remove(guess[i])
                else: #niets goed
                    continue


            if wit == 4:
                return ("congrats, you won!!")
            else:
                print(f"Er zitten {wit} pins op de goede plek en {zwart} pins zijn de goede kleur (dus niet de goede plek)")
                turnsleft -= 1
                if turnsleft == 0:
                    return ("sorry, out of turns, you lose")
                else:
                    theguess = str(guess)
                    previousguesses[theguess] = f"{wit, zwart}"
                    wit = 0
                    zwart = 0
                    guessentered = False
                    continue




#print(NewFeedbackSystem())


