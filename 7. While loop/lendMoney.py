money = 0
while True:
    if money >= 1000000:
        break
    else: 
        lend = input("Can you lend me $100000?  ")
        if lend == "yes":
            print("Thanks bro! Much appreciated!")
            money += 100000
            break
        else:
            print("Thanls a lot cheapskate!")
print("Your're rich!")
