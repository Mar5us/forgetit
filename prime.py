import math

def isPrime(number):
    prime = 1
    for i in range(3, int(math.sqrt(number))+1, 2):
        if (number%i) == 0:
            prime = 0
            break
    return prime

number = 1

while 1:
    number = number + 2
    if isPrime(number):
        print (number)



