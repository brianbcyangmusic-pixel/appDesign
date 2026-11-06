import time
money = 0
while money < 1000000:
    money += 1
    if money == 1000000:
        print("You're rich")
        break
    else:
        print("Almost there keep going. You have $" + str(money))