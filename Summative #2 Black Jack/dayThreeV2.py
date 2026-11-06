import random

mainDeck = []
currentCard = None

dealer = [1, 37, 2]
player1 = [3, 5, 1, 2, 1]
player2 = []
player3 = []

numberToWord = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King"
}

# Create the deck
for i in range(1, 53):
    mainDeck.append(i)


def drawCard():
    return mainDeck.pop(0)


def getCardIdentity(unknownCard):
    if unknownCard <= 13:
        currentCardFamily = "hearts"
    elif unknownCard <= 26:
        currentCardFamily = "diamonds"
    elif unknownCard <= 39:
        currentCardFamily = "spades"
    else:
        currentCardFamily = "clubs"

    num = (unknownCard - 1) % 13 + 1
    currentCardNum = numberToWord[num]

    return currentCardFamily, currentCardNum


def printCard(which):
    family, num = getCardIdentity(which)
    print(num, "of", family)


def printHand(who):
    for card in who:
        printCard(card)


def dealCards(who, amount):
    for i in range(amount):
        who.append(drawCard())

def playerTotalPoints(hands):
    counting =[]
    for i in hands:
        num = (i - 1) % 13 + 1
        counting.append(num)
    total = 0
    ace = 0
    for i in counting:
        if i != 1:
            if i >= 10:
                i = 10
            total += i
        else:
            ace += 1
    temp = ace
    while temp > 0:
        total += 11
        temp -= 1
    while ace > 0 and total > 21:
        total -= 10
        ace -= 1       
    return(total)


# -----------------------------------------Main code begins--------------------------------------------
random.shuffle(mainDeck)
print("----------------------------------")
print("dealer", playerTotalPoints(dealer))
print("player1", playerTotalPoints(player1))
print("----------------------------------")


print("Dealer's hand:")
printHand(dealer)

print("player1's hand:")
printHand(player1)

