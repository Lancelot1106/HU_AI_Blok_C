from random import randint
from itertools import *

code = "ABCD"

def Allcombos():

    """creates a list with all  options for the AI to choose from the first time around"""

    global allcombos

    allcombos = []

    results = product("ABCDEF", repeat=4)

    allcombos = resulttolist(results)

    return AIpicks(allcombos)

def resulttolist(result):

    """turns a result from a calculation with itertools into a list and returns it"""

    newlist = []


    for i in result:
        j = "".join(i)
        newlist.append(j)

    return newlist



def AIpicks(codes):

    AIguess = codes[0]

    print(f"Your code was {code}")
    print(f"My guess was {AIguess}")

    correct = input(str("how many did I get completely correct? "))
    semicorrect = input(str("and how many colors are right? "))

    feedback = (correct, semicorrect)
    print(feedback)

    return NewlistAI(codes, AIguess, feedback)


def auto_feedback(guess, code):

    wit = 0
    zwart = 0

    used = []

    #needed a way to split the strings from the list into lists
    Codesplit = []
    Codesplit[:0] = code



    Extracode = Codesplit.copy()



    for i in range(len(guess)):
        Guesssplit = []
        Guesssplit[:0] = guess[i]

        if guess[i] == code[i]:
            wit += 1
            used.append(i)

    for i in used:
        Extracode.remove(code[i])

    for i in range(len(guess)):
        Guesssplit = []
        Guesssplit[:0] = guess[i]

        if guess[i] in Extracode and guess[i] not in used:
            if guess[i] in Extracode:
                zwart += 1
                Extracode.remove(guess[i])
    print (wit, zwart)
    return (wit, zwart)

def NewlistAI(previouslist, guess, feedback):

    newlist = []

    for i in previouslist:
        if feedback == auto_feedback(guess, i):
            newlist.append()

    print(newlist)

    return AIpicks(newlist)


print(Allcombos())