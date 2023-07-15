def countTwoAndFive(x):
    number2 = number5 = 0
    while x % 2 == 0:
        number2 += 1
        x = x / 2
    while x % 5 == 0:
        number5 += 1
        x = x / 5
    return int(number2), int(number5)

index = n2 = n5 = 0
multi = 1
L = [100]
Number2 = []
Number5 = []

while index < len(L):
    num2, num5 = countTwoAndFive(L[index])
    Number2.append(num2)
    Number5.append(num5)
    n2 += num2
    n5 += num5
    multi *= L[index]
    index += 1

result = int(multi // (10 ** min(n2, n5))) % 2
print(result)