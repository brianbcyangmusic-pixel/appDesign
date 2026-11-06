planes = 280
xmasPlanes = 336
hours = 12
passengersPerPlane = 240
cargoPerPlane = 12
normalLate = 782
xmasLate = 1835
morningCargo = 7580
totalCargo = 12997

print("The answer to question 1 is", xmasPlanes / hours, "planes per hour")
print("The answer to question 2 is", (xmasPlanes / hours) * passengersPerPlane, "passengers per hour")
print("The answer to question 3 is", (xmasPlanes * passengersPerPlane) - (planes * passengersPerPlane), "more passengers")
print("The answer to question 4 is", xmasLate - normalLate, "more late passengers")
print("The answer to question 5 is", (832 / 32) * 5, "minutes of delay")

x = totalCargo - morningCargo
print("The answer to question 6 is", x, "tons of cargo")