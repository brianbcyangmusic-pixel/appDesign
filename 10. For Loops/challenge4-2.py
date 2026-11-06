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
    for i in range(n - 1, 0, -1):
        if isPrime(i) == True:
            return i

        
def countdownBalancedPrime(n):
    global totalBalancedPrime
    for number in range(n, 0, -1):
        if isPrime(number) == True:
            nextPrime = countUpPrime(number)
            previousPrime = countDownPrime(number)
            if previousPrime != None:
                if number - previousPrime == nextPrime - number:
                    print(number)
                    totalBalancedPrime += 1
    print("Blast off!")


while True:
    totalBalancedPrime = 0
    number = int(input("Please input a number: "))
    countdownBalancedPrime(number)
    print("There are a total of", totalBalancedPrime, "balanced prime in", number, "to 0")


    
