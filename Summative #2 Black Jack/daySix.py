import random

mainDeck = []
currentCard = None


dealer = []
player1 = []
player2 = []
player3 = []
playerList = [dealer, player1, player2, player3]

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
        who.append(mainDeck.pop(-1))

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

def isBust(hand):
    if playerTotalPoints(hand) > 21:
        return True
    return False

def is21(hand):
    if playerTotalPoints(hand) == 21:
        return True
    return False



# -----------------------------------------Main code begins--------------------------------------------

print("----------------------------")
print("Black Jack!")
print("----------------------------")
random.shuffle(mainDeck)

for i in range (0, 2):
    for i in playerList:
        dealCards(i, 1)

currentPlayer = player1
while not is21(currentPlayer) and not isBust(currentPlayer):
    userChoice = int(input("Do you want to \n 1. Hit \n 2. Stand \n"))
    if userChoice == 1:
        dealCards(currentPlayer, 1)
        print("-----------------------")
        print("Player1's deck")
        printHand(currentPlayer)
        print("Total")
        print(playerTotalPoints(currentPlayer))

        print("-----------------------")
    else:
        break

currentPlayer = dealer
while not is21(currentPlayer) and not isBust(currentPlayer):
    if playerTotalPoints(currentPlayer) <= 16:
        dealCards(currentPlayer, 1)
        print("-----------------------")
        print("dealer's deck")
        printHand(currentPlayer)
        print("Total")
        print(playerTotalPoints(currentPlayer))

        print("-----------------------")
    else:
        break








print("Dealer's hand:")
printHand(dealer)
print(playerTotalPoints(dealer))

print("player1's hand:")
printHand(player1)
print(playerTotalPoints(player1))

print("player2's hand:")
printHand(player2)
print(playerTotalPoints(player2))

print("player3's hand:")
printHand(player3)
print(playerTotalPoints(player3))





# print("----------------------------------")
# print("dealer", playerTotalPoints(dealer))
# print("player1", playerTotalPoints(player1))
# print("----------------------------------")

