def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def countDownPrime(n):
    for i in range(n, 0, -1):
        if isPrime(i) == True:
            print(i)
    print("Blast off!")
    
countDownPrime(100)