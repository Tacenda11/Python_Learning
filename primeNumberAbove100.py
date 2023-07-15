import math
def isPrime(x):
    index = 1
    for index in range(1,math.floor(math.sqrt(x))+1):
        if (x % index == 0) and (index != 1):
            return 0
        index += 1
    return 1

number = 2
for number in range(2,101):
    if isPrime(number) == 1:
        print(number, end=' ')
    number += 1