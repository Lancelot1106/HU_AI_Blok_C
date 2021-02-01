def pyramidFor(size):

    for stars in range(1, size+1):
        print('*' * stars)
    for stars in range((size-1), 0, -1):
        print('*' * stars)

def pyramidWhile(size):
    maxreached = False
    stars = 1

    while stars <= size and not maxreached:
        print('*' * stars)
        stars += 1

        if stars == size:
            maxreached = True

    while stars >= 1 and maxreached:
        print('*' * stars)
        stars -= 1

print(pyramidFor(5))
print(pyramidWhile(5))


#zin_1 = str(input("Voer een zin in: "))
#zin_2 = str(input("Voer nog een zin in: "))

def zinvergelijker(zin1, zin2):
    for i in range(0, len(zin1)):

        if zin1[i] == zin2[i]:
            continue
        else:
            return(f"Het eerste verschil zit op index: {i}")
            break

print(zinvergelijker("dit is een zin", "dit is nog een zin"))

def count(lijst, num):
    aantal = 0

    for i in range(0, len(lijst)):
        if lijst[i] == num:
            aantal += 1
        else:
            continue

    return(f"Het nummer {num} komt {aantal} keer in de lijst voor")

lijst1 = [3, 8 ,2, 3, 20, 41, 2, 3, 3, 54]

print(count(lijst1, 3))
print(count(lijst1, 2))

def verschil(lijst):
    verschil = 0

    for i in range(len(lijst)-1):
        if lijst[i] > lijst[i+1]:
            nieuwverschil = (lijst[i] - lijst[i+1])
            if nieuwverschil > verschil:
                verschil = nieuwverschil
            else:
                continue
        else:
            nieuwverschil = (lijst[i+1] - lijst[i])
            if nieuwverschil > verschil:
                verschil = nieuwverschil
            else:
                continue

    return(f"het grootste verschil is {verschil}")

print(verschil(lijst1))

foutelijst = (1, 0, 22)
regel1 = (1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0)
regel2 = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
goedelijst = (1, 1, 0, 1, 0, 1, 0, 1)


def binair(lijst):
    nullen = 0
    enen = 0

    for i in range(len(lijst)):
        if lijst[i] == 0:
            nullen += 1
        elif lijst[i] == 1:
            enen += 1
        else:
            return ("foutieve lijst \n")

    if nullen > enen:
        return(f"Er moeten meer enen dan nullen in de lijst staan, momenteel staan er {nullen} nullen en {enen} enen \n")
    elif nullen > 12:
        return(f"Er mogen max 12 nullen in de lijst staan, momenteel staan er {nullen} nullen in de lijst \n")
    else:
        return(f"Er staan {nullen} nullen en {enen} enen in de lijst \n")


print(binair(foutelijst))
print(binair(regel1))
print(binair(regel2))
print(binair(goedelijst))


def palindroom(string):
    for i in range(len(string)):
        if string[i] == string[-i - 1]:
            continue
        else:
            return("dit is geen palindroom \n")

    return(f"{string} is een palindroom \n")


print(palindroom("racecar"))
print(palindroom("racekar"))

is_sorted = lambda l: all(l[i] <= l[i+1] for i in range(len(l)-1))

def sort(lijst):
    while not is_sorted(lijst):
        for i in range(0, (len(lijst)-1)):
            if lijst[i] > lijst[i+1]:
                first = lijst[i]
                second = lijst[i+1]

                lijst[i] = second
                lijst[i+1] = first

                if is_sorted(lijst):
                    return(f"de lijst {lijst} is nu gesorteerd")
                else:
                    continue
            else:
                continue

print(sort(lijst1))

def gemiddelde(lijst):
    totaal = 0
    for i in range(len(lijst)):
        totaal += lijst[i]

    gem = totaal/len(lijst)

    return(f"het gemiddelde is {gem}")

print(gemiddelde(lijst1))


from random import randint

def getalrader():
    geraden = False
    getal = randint(0, 10)
    print(f"getal is {getal}")

    while not geraden:
        gok = int(input("Kies een geheel getal tussen 0 en 10: "))

        if gok == getal:
            geraden = True
        elif gok > 10:
            print("NIET BOVEN 10!!!")
            continue
        else:
            print("dat was niet goed, probeer opnieuw")
            continue

    if geraden:
        return(f"inderdaad, het getal was {getal}")

print(getalrader())

def replacer(string):
    replacing_dict = {
        " " : "",
        "\t" : "",
        "\n" : ""
    }

    for search, replace in replacing_dict.items():
        string = string.replace(search, replace)
    return string

def compressor(directory):
    with open(directory, "r") as file:
        text = file.read()

        newtext = replacer(text) #Moet pas weghalen VOOR de eerste letter in een regel en NA een \n

        f = open("newtext.txt", "w+")
        f.write(newtext)
        f.close()
        return

print(compressor("text.txt"))



def cycle(ch, n):
    bits = [int(i) for i in str(ch)]
    return ("".join([str(integer) for integer in (bits[n:]+bits[:n])]))


print(cycle(1101001, 3))
print(cycle(1101001, -3))
print(cycle(1101001, 0))

def fib_1(n, v0=0, v1=1):
    return fib_1(n-1, v1, v0+v1) if n > 1 else (v0, v1) [n]

print(fib_1(6))

def superGeheim():

    tekst = str(input("Voer een tekst in: "))
    rotatie = int(input("Voer een rotatie in: "))


    #En(x) = (x+n) mod ..


def FizzBuzz():
    getal = int(input("Geef een getal: "))

    if getal % 3 == 0 and getal % 5 == 0:
        return('FizzBuzz')
    elif getal % 3 == 0:
        return('Fizz')
    elif getal % 5 == 0:
        return('Buzz')
    else:
        return(getal)

print(FizzBuzz())
print(FizzBuzz())
print(FizzBuzz())
print(FizzBuzz())