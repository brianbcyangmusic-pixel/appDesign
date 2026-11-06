import random
carBrands = ["Hummer", "Saab", "Pontiac", "Plymouth", "Rover", "Dodge"]
randomCars = []
amountCars = []
counts = 0

for i in range(0, 100):
    randomCars.append(carBrands[random.randint(0,5)])

def printCars():
    for i in range(0, len(randomCars)):
        print((i + 1), randomCars[i])

def numOfBrand(choosenBrand):
    counts = 0
    for i in randomCars:
        if choosenBrand == i:
            counts += 1
    return counts
printCars()
print()
print()
print()
iii = input("give me a car brand: ")
print("There are", numOfBrand(iii), iii,"cars in random car list!")

for i in carBrands:
    amountCars.append(numOfBrand(i))
def mostPopularCar():
    global biggest_number
    biggest_number = amountCars[0]

    for num in amountCars:
        if num > biggest_number:
            biggest_number = num
    idBig = amountCars.index(biggest_number)
    return carBrands[idBig]

def leastPopularCar():
    global smallest_number
    smallest_number = amountCars[0]

    for num in amountCars:
        if num < smallest_number:
            smallest_number = num

    idSmall = amountCars.index(smallest_number)
    return carBrands[idSmall]

print("The most popular brand is", mostPopularCar())
print("The least popular brand is", leastPopularCar())
print("the difference is", biggest_number - smallest_number)



