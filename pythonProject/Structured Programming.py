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
            print(f"Het eerste verschil zit op index: {i}")
            break

print(zinvergelijker("dit is een zin", "dit is nog een zin"))

def count(lijst, num):
    aantal = 0

    for i in range(0, len(lijst)):
        if lijst[i] == num:
            aantal += 1
        else:
            continue

    print(f"Het nummer {num} komt {aantal} keer in de lijst voor")

lijst1 = (3, 8 ,2, 3, 20, 41, 2, 3, 3, 54)

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

    print(f"het grootste verschil is {verschil}")

print(verschil(lijst1))