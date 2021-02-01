gamestarted = False
play = 0  # 0 for unselect, 1 for guess, 2 for code

print("welcome")

def welcome():
    global gamestarted
    global gamequit
    global play

    while not gamestarted:
        upforgame = str(input("are you up for a game? (yes/no) ")).lower()
        if upforgame == "yes":
            print("GREAT!")
            while upforgame == "yes":
                side = str(input("do you want to guess or make the code? (guess/code) ")).lower()
                if side == "guess":
                    print("good luck, and enjoy")
                    return (functie)
                elif side == "code":
                    print("good luck, and enjoy")
                    return (functie)
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

print(welcome())

#def 
#player creates the code -->

    #speler creert code

        #while not win or lose

            #AI geeft een code volgens strategie

                #speler geeft feedback

                    #win/verlies?

                    #terug naar begin loop


#player guesses the code -->

    #code = [randint(1, 6), randint(1,6), randint(1,6), randint(1,6)]

        #while not win or lose

            #input: xxx, xxx, xxx, xxx

                #kijk welke xxx is goed + goede plek?

                    #win?

                #kijk welke xxx is goed + niet goede plek?

                    #verlies?

                    #feedback, turncounter -1 en terug naar begin while

