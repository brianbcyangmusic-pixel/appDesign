items = ["burgers", "wraps", "hot dogs", "salads", "cokes", "coffees", "orange juices", "French Fries", "onion rings"]
items_left = []
comboA = 0
comboB = 0
comboC = 0
comboD = 0

def checkItemNotExists(i):
    if i in items_left:
        return False
    else:
        return True


print("------------------------------------")
print("Welcome to Krusty Burger!")
print("------------------------------------")


print("How many burgers would you like to order?")
burgers = int(input())
print("How many wraps would you like to order?")
wraps = int(input())
print("How many hot dogs would you like to order?")
hot_dogs = int(input())
print("How many salads would you like to order?")
salads = int(input())
print("How many cokes would you like to order?")
cokes = int(input())
print("How many coffees would you like to order?")
coffees = int(input())
print("How many orange juices would you like to order?")
orange_juices = int(input())
print("How many French Fries would you like to order?")
french_fries = int(input())
print("How many onion rings would you like to order?")
onion_rings = int(input())

item_var = {
    "burgers": burgers,
    "wraps": wraps,
    "hot dogs": hot_dogs,
    "salads": salads,
    "cokes": cokes,
    "coffees": coffees,
    "orange juices": orange_juices,
    "French Fries": french_fries,
    "onion rings": onion_rings
}

while (burgers > 0 and (french_fries > 0 or onion_rings > 0) and (coffees > 0 or orange_juices > 0 or cokes > 0)):
    comboA += 1
    burgers -= 1
    if french_fries > 0:
        french_fries -= 1
    else:
        onion_rings -= 1
    if coffees > 0:
        coffees -= 1
    elif orange_juices > 0:
        orange_juices -= 1
    else:
        cokes -= 1

while (wraps > 0 and (french_fries > 0 or onion_rings > 0) and (coffees > 0 or orange_juices > 0 or cokes > 0)):
    comboB += 1
    wraps -= 1
    if french_fries > 0:
        french_fries -= 1
    else:
        onion_rings -= 1
    if coffees > 0:
        coffees -= 1
    elif orange_juices > 0:
        orange_juices -= 1
    else:
        cokes -= 1

while(hot_dogs > 0 and (french_fries > 0 or onion_rings > 0) and (coffees > 0 or orange_juices > 0 or cokes > 0)):
    comboC += 1
    hot_dogs -= 1
    if french_fries > 0:
        french_fries -= 1
    else:
        onion_rings -= 1
    if coffees > 0:
        coffees -= 1
    elif orange_juices > 0:
        orange_juices -= 1
    else:
        cokes -= 1

while(salads > 0 and (french_fries > 0 or onion_rings > 0) and (coffees > 0 or orange_juices > 0 or cokes > 0)):
    comboD += 1
    salads -= 1
    if french_fries > 0:
        french_fries -= 1
    else:
        onion_rings -= 1
    if coffees > 0:
        coffees -= 1
    elif orange_juices > 0:
        orange_juices -= 1
    else:
        cokes -= 1

print("RECEIPT")
print("------------------------------------")
print("combos ordered:")
print("Combo A---------------------- $5.50 x ", comboA, " = $",comboA * 5.50)
print("Combo B---------------------- $4.50 x ", comboB, " = $", comboB * 4.50)
print("Combo C---------------------- $4.00 x ", comboC, " = $", comboC * 4.00)
print("Combo D---------------------- $3.50 x ", comboD, " = $", comboD * 3.50)

for i in items:
    food = item_var[i]
    if food > 1 and checkItemNotExists(i):
        items_left.append(i)

print("individual items ordered:")
for i in items_left:
    if i == "burgers":
        print("Burgers---------------------- $3.99 x ", burgers, " = $", burgers * 3.99)
    elif i == "wraps":
        print("Wraps------------------------ $3.00 x ", wraps, " = $", wraps * 3.00)
    elif i == "hot dogs":
        print("Hot Dogs--------------------- $2.00 x ", hot_dogs, " = $", hot_dogs * 2.00)
    elif i == "salads":
        print("Salads----------------------- $2.50 x ", salads, " = $", salads * 2.50)
    elif i == "French Fries":
        print("French Fries----------------- $1.50 x ", french_fries, " = $", french_fries * 1.50)
    elif i == "onion rings":
        print("Onion Rings------------------ $1.50 x ", onion_rings, " = $", onion_rings * 1.50)
    elif i == "coffees":
        print("Coffees---------------------- $1.50 x ", coffees, " = $", coffees * 1.50)
    elif i == "orange juices":
        print("Orange Juices----------------- $1.00 x ", orange_juices, " = $", orange_juices * 1.00)
    elif i == "cokes":
        print("Cokes------------------------ $1.00 x ", cokes, " = $", cokes * 1.00)




