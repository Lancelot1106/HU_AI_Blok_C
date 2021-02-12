from random import randint, choice
from itertools import *


gamestarted = False
feedbackgiven = False
soclose = False
all_right = False

allnums = [1, 2, 3, 4, 5, 6]
choicelist = []
colorcode = []
notnum = []
allcombos = []
usedcombos = []
Code = []

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

                    return (CreateCode())

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




def resulttolist(result, feedback = 0):

    """turns a result from a calculation with itertools into a list and returns it"""

    newlist = []

    if feedback == 2:
        for i in result:
            j = " ".join(i)
            k = list(j.split(" "))
            newlist.append(k)
    elif feedback == 3:
        for i in result:
            j = " ".join(i)
            k = list(j.split(" "))
            newlist.append(k)
    else:
        for i in result:
            j = "".join(i)
            newlist.append(j)

    return newlist



def compareWithAll(lijst, previouslist, feedback = 0):

    """creates a list with options, takes out previously attempted guesses and compared to the code impossible guesses, resulting in less options to choose"""

    global usedcombos

    results = []


    if feedback == 2: #to make sure there's a 2 letter combination with gaps
        for i in previouslist:
            for letter1, letter2 in lijst:
                if letter1 in i and letter2 in i:
                    results.append(i)

    elif feedback == 3: #to make sure there's a 3 letter combination with gaps
        for i in previouslist:
            for letter1, letter2, letter3 in lijst:
                if letter1 in i and letter2 in i and letter3 in i:
                    results.append(i)
    else:
        for i in previouslist:

            for j in range(len(lijst)):

                if lijst[j] in i:

                    results.append(i)

    results = [item for item in results if item not in usedcombos]
    results = list(dict.fromkeys(results))

    print(f"It seems I only {len(results)} options left!")

    return AIguessing(results)



def Allcombos():

    """creates a list with all 1269 options for the AI to choose from the first time around"""

    global allcombos

    allcombos = []

    results = product("ABCDEF", repeat=4)

    allcombos = resulttolist(results)

    return AIguessing(allcombos)



def CreateCode():

    """Code creator, currently uses ABCDEF instead of colors, which will be added later including the check"""

    global Code

    colors = ["black", "white", "red", "green", "yellow", "blue"]
    codepicked = False

    print("good to see you")
    print("want to test the limits of my knowledge?")

    while not codepicked:
        #print("The possible colors for a code are: Red, Blue, Yellow, Green, Black and White")
        Code = (str(input("Choose the colors (letters) for your code: ")))

        return Allcombos()



def AIguessing(lijst):

    """AI picks a random option from the list, presents it to the player who will give feedback on the code. Includes a simple check for false feedback (if more than 5 'pins')"""

    global Code
    global allcombos


    AIguess = choice(lijst)

    print(f"The original code was {Code}")
    print(f"my guess this time is {AIguess}, how did I do?")
    while not feedbackgiven:
        correct = int(input("Write down how many colors are in the right spot: "))
        semicorrect = int(input("Write down how many colors are correct but not in the right spot: "))

        feedback = correct + semicorrect
        if feedback <= 4:
            return NewFeedbackSystem(AIguess, correct, semicorrect, lijst)
        else:
            print("please use numbers 1-4 where the total <= 4")
            continue



def NewFeedbackSystem(guess, correct, semicorrect, lijst):

    """Creme de la creme, this system checks the amount of feedback given and creates a list with the possible options according to that feedback"""

    global allcombos
    global usedcombos
    global all_right


    feedback = correct + semicorrect

    usedcombos.append(guess)

    if not allright: #needs an extra way to AT LEAST get the same feedback as previous one

        if feedback == 4: #takes all letters in the code and checks for possible new combinations, adds them to the list
            for j in range(1):
                A = guess[j]
                B = guess[j + 1]
                C = guess[j + 2]
                D = guess[j + 3]

            results = permutations(f"{A}{B}{C}{D}", 4)
            newcombos = resulttolist(results)
            newcombos = [item for item in newcombos if item not in usedcombos]

            all_right = True
            return AIguessing(newcombos)

        elif feedback == 3: #takes all letters in the code and checks for possible new combinations with >= 3 from previous code, adds them to the list
            results = permutations(guess, 3)
            newresult = resulttolist(results, feedback)

            return compareWithAll(newresult, lijst, feedback)

        elif feedback == 2:
            #takes all letters in the code and checks for possible new combinations with >= 2 from previous code, adds them to the list
            results = permutations(guess, 2)
            newresult = resulttolist(results, feedback)

            return compareWithAll(newresult, lijst, feedback)

        elif feedback == 1:
            #takes all letters in the code and checks for possible new combinations with >= 1 from previous code, adds them to the list
            results = combinations(guess, 1)
            newresult = list(dict.fromkeys(resulttolist(results)))


            return compareWithAll(newresult, lijst)

        else:
            #takes all letters in the code and checks for possible new combinations WITHOUT these letters, adds them to the list
            newletterlist = [item for item in letters if item not in guess] #creates a new list with letters that weren't used
            newletters = "".join(newletterlist)

            results = product(newletters, repeat=4)
            newcombos = resulttolist(results)
            newcombos = [item for item in newcombos if item not in usedcombos]

            return AIguessing(newcombos)

    else: #if all letters were guessed correctly

        if correct == 4:
            return ("Well played Human, but I win this time")

        elif correct == 2: #in a 2,2 case, checks which combinations are possible while keeping 2 on the same spot each time

            results = permutations(guess, 2)
            newresult = resulttolist(results, feedback)

            return compareWithAll(newresult, lijst, feedback)

        elif correct == 1: #in a 1,3 case, creates a list with still possible combinations (since there'll be only 8, it's hardcoded in here)
            for j in range(1):
                A = guess[j]
                B = guess[j + 1]
                C = guess[j + 2]
                D = guess[j + 3]

                newcombos = [f"{A}{C}{D}{B}", f"{A}{D}{B}{C}", f"{C}{B}{D}{A}", f"{D}{B}{A}{C}", f"{B}{D}{C}{A}", f"{D}{A}{C}{B}", f"{B}{C}{A}{D}", f"{C}{A}{B}{D}"]
                newcombos = [item for item in newcombos if item not in usedcombos]

                return AIguessing(newcombos)

        else:
            for j in range(1):
                A = guess[j]
                B = guess[j + 1]
                C = guess[j + 2]
                D = guess[j + 3]

            results = permutations(f"{A}{B}{C}{D}", 4)
            newcombos = resulttolist(results)
            newcombos = [item for item in newcombos if item not in usedcombos]

            return AIguessing(newcombos)















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
            codeExtra = code.copy()
            usedcolors = []

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




print(welcome())


