def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countUpPrime(n):
    for i in range(n + 1, 2147483647, +1):
        if isPrime(i) == True:
            return i

def countDownPrime(n):
    for i in range(n - 1, -2147483647, -1):
        if isPrime(i) == True:
            return i


while True:
    number = int(input("please input a prime number: "))
    if isPrime(number) == True:
        print(number, "is prime")
    else:
        print(number, "is not prime, try again!!!")
        continue
    nextPrime = countUpPrime(number)
    previousPrime = countDownPrime(number)
    print("The next primt is", nextPrime)
    print("The previous prime is", previousPrime)
    print("----------------")
    print("The gap below it is: ", number - previousPrime)
    print("The gap above it is: ", nextPrime - number)
    if number - previousPrime == nextPrime - number:
        print("----------------")
        print("This number is a balanced prime.")
        print("----------------")
    else:
        print("----------------")
        print("Not this one")
        print("----------------")
